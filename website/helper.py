from datetime import datetime
import requests
import urllib.request
import json
from dataMining.helper import validate, BASE_URL, getIndicatorName
from collections import defaultdict
from dataMining.models import Indicator

# ==========================
# IMPORTS FROM DATA MINING
# ==========================

def checkList(urls, year):
#   Helper for getRecentOfAll
    for url in urls:
        if not validate(url)['exists']:
            return False
    return True

def getRecentOfAll(ids):
    
    temp_year = datetime.now().year
    end_year = temp_year - 20
    
    while(end_year < temp_year):
        urls = []
        for id in ids:
            urls.append(BASE_URL + "countries/indicators/"+ id + "?date=" + str(temp_year) + "&format=json")

        if checkList(urls, temp_year):
            return temp_year
        temp_year -= 1
        
    return False


def handleData(request, year, ids, coefs, opers):

    data = []

    for i in range(len(ids)):
        my_id = ids[i]
        my_weight = coefs[i]

        my_url = "http://" + request.get_host() + "/api/" + my_id + "/" + str(year) + "/" + str(my_weight)

        with urllib.request.urlopen(my_url) as url:
            result = json.loads(url.read().decode())['result']
            data.append(result)

    data = beautify(data, ids, coefs, opers)
    data = onlyAvailable(data, ids)

    # SORT CAN BE DONE IN THE FRONTEND
    # data = sortFormat(data)

    return data

def beautify(data, ids, coefs, opers):

    newDict = {}

    for i in range(len(data)):
        for key, value in data[i].items():
            newDict[key] = {}
            newDict[key]['final'] = 1

    for i in range(len(data)):
        for key, value in data[i].items():
            newDict[key]['name'] = data[i][key]['country']
            newDict[key]['id_'+str(i)] = {"id":ids[i],"value":data[i][key]['value'], "pre_assign":data[i][key]['index']**(1/float(coefs[i])), "post_assign":data[i][key]['index']}

            if i == 0:
                newDict[key]['final'] *= newDict[key]['id_'+str(i)]['post_assign']
            elif i > 0:
                if opers[i-1] == "*":
                    newDict[key]['final'] *= newDict[key]['id_'+str(i)]['post_assign']
                elif opers[i-1] == "+":
                    newDict[key]['final'] += newDict[key]['id_'+str(i)]['post_assign']

            #data[i][key]['country']
            #data[i][key]['value']
            #data[i][key]['index']

    return newDict

def onlyAvailable(data, ids):
    
    for i in range(len(ids)):
        for key in list(data.keys()):
            if "id_"+str(i) not in list(data[key].keys()):
                del data[key]

    return data

def sortFormat(data):

    newData = []

    sorted_keys = sorted((value['final'], key) for (key,value) in data.items())

    for i in sorted_keys:
        newData.insert(0, data[i[1]])

    return newData

def getIndicatorNames(indicators):

    indicatorNames = []

    for indicator in indicators:
        indicatorNames.append(Indicator.objects.get(my_id=indicator).name)

    return indicatorNames

from datetime import datetime
import requests
import urllib.request
import json
from dataMining.helper import validate, BASE_URL, getIndicatorName
from collections import defaultdict
from dataMining.models import Indicator
from website.models import Interaction
from ast import literal_eval

# ==========================
# IMPORTS FROM DATA MINING
# ==========================
def getInteractions():
    return Interaction.objects.count()

def smaller_json_data(string_data):
    data = literal_eval(string_data)

    del data['count_interactions']

    return data

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
    data = sortFormat(data)
    data = setUNDP(request, data, year)

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
                if opers[i-1] == "×":
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
    country_keys = [key for key in data.keys()]
    country_vals = [country['final'] for country in data.values()]
    country_hdis = list(zip(country_keys, country_vals))

    sorted_ranks = sorted(country_hdis, key=lambda tup: tup[1], reverse=True)

    for key, country in data.items():
        for item in sorted_ranks:
            if key == item[0]:
                country['rank'] = sorted_ranks.index(item) + 1

    return data

def setUNDP(request, data, year):

    my_url = "http://" + request.get_host() + "/api/undp/"+getUNDPYear(request, year)

    with urllib.request.urlopen(my_url) as url:
        result = json.loads(url.read().decode())['result']

        for key, country in data.items():
            try:
                country['undp'] = result[key]
            except:
                country['undp'] = "N/A"

    return data

def getUNDPYear(request, year):
    
    my_url = "http://" + request.get_host() + "/api/undp/"

    my_year=year
    while my_year >= 1990:
        with urllib.request.urlopen(my_url+str(my_year)) as url:
            result = json.loads(url.read().decode())['result']
            if result:
                return str(my_year)
        my_year -= 1
    return False

def getIndicatorNames(indicators):

    indicatorNames = []

    for indicator in indicators:
        indicatorNames.append(Indicator.objects.get(my_id=indicator).name)

    return indicatorNames

from datetime import datetime
import requests
import urllib.request
import json
from dataMining.helper import validate, BASE_URL, getIndicatorName
from collections import defaultdict

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


def handleData(request, year, ids, coefs):

    data = []

    for i in range(len(ids)):
        my_id = ids[i]
        my_weight = coefs[i]

        my_url = "http://" + request.get_host() + "/api/" + my_id + "/" + str(year) + "/" + str(my_weight)
        # temp = requests.get(url=url).json()
        with urllib.request.urlopen(my_url) as url:
            result = json.loads(url.read().decode())['result']
            data.append(result)

    data = beautify(data, ids)

    return data

def beautify(data, ids):

    newDict = {}

    for i in range(len(data)):
        for key, value in data[i].items():
            newDict[key] = {}

    for i in range(len(data)):
        for key, value in data[i].items():
            newDict[key]['country'] = data[i][key]['country'] 
            #data[i][key]['country']
            #data[i][key]['value']
            #data[i][key]['index']

    return newDict
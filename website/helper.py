from datetime import datetime
import requests
import urllib.request
import json
from dataMining.helper import validate, BASE_URL

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

        my_url = "http://" + request.get_host() + "/api/" + my_id + "/" + str(year)
        # temp = requests.get(url=url).json()
        with urllib.request.urlopen(my_url) as url:
            result = json.loads(url.read().decode())['result']
            temp = updateIndices(result, my_weight)
            data.append(temp)

    return data
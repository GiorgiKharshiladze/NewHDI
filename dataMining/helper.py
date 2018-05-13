import requests
from datetime import datetime

BASE_URL = "http://api.worldbank.org/v2/"

def validate(url): # Checks if data exists on this url
    result = {}
    data = requests.get(url=url).json()
    if 'total' in data[0].keys():
        amount = data[0]['total']
        result['url'] = url + "&per_page=" + str(amount)
        result['exists'] = False
        if amount > 0 and data[1][0]['value'] != None:
            result['exists'] = True
    else:
        result['exists'] = False
    return result

def getRecent(id): # Gets the most recent data available (if exists)
    temp_year = datetime.now().year
    end_year = temp_year - 20
    
    while(end_year < temp_year):
        url = BASE_URL + "countries/indicators/" + id + "?date=" + str(temp_year) + "&format=json"
        if validate(url)['exists']:
            return validate(url)['url']
        temp_year -= 1
    return False

def getData(id):
    result = []
    url = getRecent(id)
    if url:
        data = requests.get(url=url).json()
        for item in data[1]:
            if item['countryiso3code'] != "":
                # Just countries not aggregates
                result.append(item)
        return result
    else:
        return False # There is no data available
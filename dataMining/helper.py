import requests
import json
from datetime import datetime
import sys

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

def getMinMaxActual(id, my_country):
    
    countries = getData(id)
    minimum = sys.maxsize
    maximum = -sys.maxsize -1

    for country in countries:
        if country['countryiso3code'] == my_country:
            actual = country['value'] or False
        if country['value'] != None:
            if country['value'] < minimum:
                minimum = country['value']
            if country['value'] > maximum:
                maximum = country['value']

    return {"actual": actual,"max":maximum, "min":minimum}

def calculateIndex(id, my_country):

    data = getMinMaxActual(id, my_country)
    actual = data['actual']
    maximum = data['max']
    minimum = data['min']

    if actual:
        return (actual-minimum)/(maximum-minimum) # formula to calculate index
    else:
        return False # No data available

print(calculateIndex("SP.DYN.LE00.IN", "GEO"))
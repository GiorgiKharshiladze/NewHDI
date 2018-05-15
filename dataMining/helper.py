import requests
import json
import sys

BASE_URL = "http://api.worldbank.org/v2/"

def validate(url):
#   Checks if data exists on this url
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

def getData(id, year):
    result = []

    url = validate(BASE_URL + "countries/indicators/" + id + "?date=" + str(year) + "&format=json")['url']
    if validate(url)['exists']:
        data = requests.get(url=url).json()
        for item in data[1]:
            if item['countryiso3code'] != "":
                # Just countries not aggregates
                result.append(item)
        return result
    else:
        return False # There is no data available

def getMinMaxActual(id, year, my_country):
    
    countries = getData(id, year)
    minimum = sys.maxsize
    maximum = -sys.maxsize -1

    actual = False

    for country in countries:
        if country['countryiso3code'] == my_country:
            actual = country['value']
        if country['value'] != None:
            if country['value'] < minimum:
                minimum = country['value']
            if country['value'] > maximum:
                maximum = country['value']

    return { "actual": actual, "max": maximum, "min": minimum }

def calculateIndex(id, year, my_country):

    data = getMinMaxActual(id, year, my_country)
    actual = data['actual']
    maximum = data['max']
    minimum = data['min']

    if actual:
        index = (actual-minimum)/(maximum-minimum) # formula to calculate index
        return (data, index) # tuple of data and formula result sent for json conversion
    else:
        return False # No data available

# print(calculateIndex("SP.DYN.LE00.IN", "GEO"))
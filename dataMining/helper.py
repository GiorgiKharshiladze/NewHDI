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
    result = {}

    # IF id is invalid URL key does not exist. NEEDS TO BE FIXED
    validation = validate(BASE_URL + "countries/indicators/" + id + "?date=" + str(year) + "&format=json")
    if validation['exists']:
        if validate(validation['url'])['exists']:
            data = requests.get(url=validation['url']).json()

            for item in data[1]:
                if item['countryiso3code'] != "" and item['value'] != None:
                    # Just countries not aggregates and only those which data exists
                    result[item['countryiso3code']] = item
            return result
    else:
        return False # There is no data available

def getCleanData(id, year):

    minmax = []
    countries = getData(id, year)

    if not countries:
        return False

    for i in countries.values():
        if i['value']:
            minmax.append(i['value'])

    minimum = min(minmax)
    maximum = max(minmax)

    # Get Indicator Name
    indicator = getIndicatorName(countries)

    for country in countries.values():
        country = clean(country)
        if country['value']:
            country['index'] = calculate(country['value'], maximum, minimum)
        else:
            country['index'] = None

    countries['info'] =  {"id":id, "indicator":indicator, "year":year}

    return countries

def getInfo(id, year, my_country):
    
    countries = getCleanData(id, year)
    if not countries:
        return False

    return countries.get(my_country, False)

def calculate(actual, maximum, minimum):
    # We can have separate special cases here i.e LOG, Education etc.
    formula = (actual-minimum)/(maximum-minimum)

    return formula

def clean(item):
#   This function beautifies our json
    # item['id'] = item['indicator']['id']
    # item['indicator'] = item['indicator']['value']
    item['country'] = item['country']['value']
    # item['country_id'] = item['countryiso3code']

    # Remove
    del item['date']
    del item['indicator']
    del item['countryiso3code']
    del item['unit']
    del item['obs_status']
    del item['decimal']

    return item

def getIndicatorName(countries):

    for key in countries:
        return countries[key]['indicator']['value']

# print(calculateIndex("SP.DYN.LE00.IN", "GEO"))
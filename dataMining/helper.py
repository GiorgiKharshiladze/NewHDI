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

    # IF id is invalid URL key does not exist. NEEDS TO BE FIXED
    validation = validate(BASE_URL + "countries/indicators/" + id + "?date=" + str(year) + "&format=json")
    if validation['exists']:
        if validate(validation['url'])['exists']:
            data = requests.get(url=validation['url']).json()

            for item in data[1]:
                if item['countryiso3code'] != "":
                    # Just countries not aggregates
                    result.append(item)
            return result
    else:
        return False # There is no data available

def getCleanData(id, year):

    minmax = []
    countries = getData(id, year)

    for i in countries:
        if i['value']:
            minmax.append(i['value'])

    minimum = min(minmax)
    maximum = max(minmax)

    for country in countries:
        country = clean(country)
        if country['value']:
            country['index'] = (country['value'] - minimum)/(maximum - minimum)
        else:
            country['index'] = None

    return countries

def getInfo(id, year, my_country):
    
    countries = getCleanData(id, year)
    minimum = sys.maxsize
    maximum = -sys.maxsize -1

    actual = False
    for country in countries:
        if country['country_id'] == my_country:
            actual = country['value']
            name = country['country']
            indicator = country['indicator']
        if country['value'] != None:
            if country['value'] < minimum:
                minimum = country['value']
            if country['value'] > maximum:
                maximum = country['value']
    if not actual:
        return False

    return {"id": id, "indicator": indicator, "country": name, "date": year, "actual": actual, "max": maximum, "min": minimum }

def calculateIndex(id, year, my_country):

    data = getInfo(id, year, my_country)

    if data:    
        actual = data['actual']
        maximum = data['max']
        minimum = data['min']
        index = (actual-minimum)/(maximum-minimum) # formula to calculate index

        return (data, index) # tuple of data and formula result sent for json conversion
    else:
        return False # No data available

def clean(item):
#   This function beautifies our json
    item['id'] = item['indicator']['id']
    item['indicator'] = item['indicator']['value']
    item['country'] = item['country']['value']
    item['country_id'] = item['countryiso3code']

    # Remove
    del item['countryiso3code']
    del item['unit']
    del item['obs_status']
    del item['decimal']

    return item

# print(calculateIndex("SP.DYN.LE00.IN", "GEO"))
import requests
import json
import sys
from copy import deepcopy
from dataMining.models import Indicator
import numpy as np

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
    # indicator = getIndicatorName(id)

    for country in countries.values():
        country = clean(country)
        if country['value'] != None:
            country['index'] = calculate(country['value'], maximum, minimum, id)
        else:
            country['index'] = None

    # countries['info'] =  {"id":id, "indicator":indicator, "year":year}

    return countries

def getInfo(id, year, my_weight):
    
    countries = getCleanData(id, year)
    if not countries:
        return False

    return updateIndices(countries, my_weight)

def calculate(actual, maximum, minimum, id):
    # We can have separate special cases here i.e LOG, Education etc.

    formula = (actual-minimum)/(maximum-minimum)

    isProportional = Indicator.objects.get(my_id=id).proportional

    if not isProportional:
        formula = 1 - formula

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

def getIndicatorName(id):

    data = requests.get(url=BASE_URL + "countries/indicators/" + id + "/?format=json").json()
    return data[1][0]['indicator']['value'] or False


def updateIndices(countries, weight):

    for key in countries.keys():
        countries[key]['index'] **= float(weight)

    return countries

# print(calculateIndex("SP.DYN.LE00.IN", "GEO"))

# UNDP Data Mining
import pandas as pd

def getFormatedUNDP(file_name):

    my_undp = {}
    df = pd.read_csv(file_name, index_col="Country")
    df = df.fillna(0)

    country_list = list(df.index)

    for col in df.columns:
        my_undp[col] = {}
        for country in country_list:
            my_undp[col][country] = df.loc[country, col]

    return my_undp
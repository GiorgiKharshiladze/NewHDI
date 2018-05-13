from django.shortcuts import render
import requests
from datetime import datetime

# Create your views here.

BASE_URL = "http://api.worldbank.org/v2/countries/indicators/"

def api(request):
	
	test_url = "http://api.worldbank.org/v2/indicators?format=json"
	per_page = requests.get(url=test_url).json()[0]['total']

	my_url = test_url + "&per_page="+str(per_page)
	result = requests.get(url=my_url).json()[1]


	return render(request, "api.html", {"result": result})

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
        url = BASE_URL + id + "?date=" + str(temp_year) + "&format=json"
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


# ============================================
# REMOVED: Fill in the indicators to local db
# ============================================
# def fill_indicators_table(request):

# 	test_url = "http://api.worldbank.org/v2/indicators?format=json"
# 	per_page = requests.get(url=test_url).json()[0]['total']

# 	my_url = test_url + "&per_page="+str(per_page)
# 	r = requests.get(url=my_url)
# 	counter = 0
# 	for i in r.json()[1]:
# 		# print(i["id"]) # indicator_id
# 	    # print(i["source"]["value"]) # title
# 	    # print(i["sourceNote"]) # description

# 		new_indicator = Indicator(indicator_id=i["id"], title=i["source"]["value"], description=i["sourceNote"])

# 		counter += 1
# 		print(str(counter)+ ": " + str(new_indicator))

# 		new_indicator.save()

# 	return None
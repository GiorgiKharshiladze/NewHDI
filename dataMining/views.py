from django.shortcuts import render
from django.http import HttpResponse
from dataMining.helper import *

# Create your views here.

def preMine(request):
	
	test_url = BASE_URL + "indicators?format=json"
	per_page = requests.get(url=test_url).json()[0]['total']

	my_url = test_url + "&per_page="+str(per_page)
	result = requests.get(url=my_url).json()[1]


	return render(request, "preMine.html", {"result": result})

def getIndicator(request, id, year):

	data = getCleanData(id, year)

	if data:
		dump = json.dumps({"result": data})
	else:
		dump = json.dumps({"result": False}) # No data available


	# return render(request, "index.html", {"data": data})
	return HttpResponse(dump, content_type='application/json')

def getIndex(request, id, year, my_country):

	data = getInfo(id, year, my_country)

	if data:
		dump = json.dumps({"result": data})
	else:
		dump = json.dumps({"result": False})

	return HttpResponse(dump, content_type='application/json')

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
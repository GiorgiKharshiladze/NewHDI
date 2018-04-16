from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Indicator
from .serializers import IndicatorSerializer

# import requests

# Create your views here.

def api(request):
	
	test_url = "http://api.worldbank.org/v2/indicators?format=json"
	per_page = requests.get(url=test_url).json()[0]['total']

	my_url = test_url + "&per_page="+str(per_page)
	result = requests.get(url=my_url)

	return render(request, "index.html", {"result": result})


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
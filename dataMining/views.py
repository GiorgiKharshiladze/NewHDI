from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.templatetags.staticfiles import static

# local improts
from .helper import *
from .serializers import *
from .models import *

# rest_framework
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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

def getValue(request, id, year, my_weight):

	data = getInfo(id, year, my_weight)

	if data:
		dump = json.dumps({"result": data})
	else:
		dump = json.dumps({"result": False})

	return HttpResponse(dump, content_type='application/json')

def getUNDP(request):

	url = request.build_absolute_uri().replace(request.get_full_path(), "")

	try:
		data = getFormatedUNDP(url + static('undp_formated.csv'))
	except:
		data = False

	dump = json.dumps({"result": data})

	return HttpResponse(dump, content_type='application/json')

def getUNDP_Year(request, year):

	url = request.build_absolute_uri().replace(request.get_full_path(), "")
	
	try:
		data = getFormatedUNDP(url + static('undp_formated.csv'))[year]
	except:
		data = False

	dump = json.dumps({"result": data})

	return HttpResponse(dump, content_type='application/json')


@api_view(['GET'])
def getLocalIds(request):

	indicator = Indicator.objects.all()

	serializer = IndicatorSerializer(indicator, many=True)

	return Response(serializer.data)

@api_view(['GET'])
def getLocal(request, my_id):

	try:
		indicator = Indicator.objects.get(my_id=my_id)
	except Indicator.DoesNotExist:
		return HttpResponse(json.dumps({"result": False}), content_type='application/json')

	serializer = IndicatorSerializer(indicator)

	return Response(serializer.data)
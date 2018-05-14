from django.shortcuts import render
from website.helper import *

# Create your views here.

def index(request):

	return render(request, "index.html")

def dashboard(request):

	return render(request, "dashboard.html")

def test(request):

	ids = ["","","",""]

	year = getRecentOfAll(ids)
	
	data = requests.get(url=url)

	return render(request, "test.html", {"data":data})

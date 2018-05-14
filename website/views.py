from django.shortcuts import render
from website.helper import *

# Create your views here.

def index(request):

	return render(request, "index.html")

def dashboard(request):

	return render(request, "dashboard.html")

def test(request):
    # GNI per capita, PPP (constant 2011 international $) (NY.GNP.PCAP.PP.KD)
    # GDP per capita, PPP (constant 2011 international $) (NY.GDP.PCAP.PP.KD)
    # Life expectancy at birth, total (years) (SP.DYN.LE00.IN)
    # UIS: Mean years of schooling of the population age 25+. Male (UIS.EA.MEAN.1T6.AG25T99.M) - NOT AVAILABLE

    ids = ["NY.GDP.PCAP.PP.KD","SP.DYN.LE00.IN","NY.GNP.PCAP.PP.KD"]

    year = getRecentOfAll(ids)

    url = "http://" + request.get_host() + "/api/" + str(year) + "/" + ids[2]
    data = requests.get(url=url).json()

    return render(request, "test.html", {"data":data})

from django.shortcuts import render
from django.http import HttpResponse
from website.helper import *
import urllib.request

# Create your views here.

def index(request):

    indicators = {"NY.GNP.PCAP.PP.KD" : "GNI per capita, PPP (constant 2011 international $)","NY.GDP.PCAP.PP.KD" : "GDP per capita, PPP (constant 2011 international $)", "SP.DYN.LE00.IN":"Life expectancy at birth, total (years)", "SE.XPD.TOTL.GD.ZS":"Government expenditure on education, total (% of GDP)", "TX.VAL.OTHR.ZS.WT":"Computer, communications and other services (% of commercial service exports)"}
    
    return render(request, "main.html", {"indicators":indicators})

def customHDI(request):

    ids = [request.POST.get('ind1'),request.POST.get('ind2'),request.POST.get('ind3'),request.POST.get('ind4'),request.POST.get('ind5')]
    coefs = [request.POST.get('coef1'),request.POST.get('coef2'),request.POST.get('coef3'),request.POST.get('coef4'),request.POST.get('coef5')]

    year = getRecentOfAll(ids)
    
    # Handle form data here
    data = handleData(request, year, ids, coefs)

    dump = json.dumps({"result": data})
    return HttpResponse(dump, content_type='application/json')
    # return render(request, "custom.html", {"data":data})

def dashboard(request):

	return render(request, "dashboard.html")

def test(request):
    # GNI per capita, PPP (constant 2011 international $) (NY.GNP.PCAP.PP.KD)
    # GDP per capita, PPP (constant 2011 international $) (NY.GDP.PCAP.PP.KD)
    # Life expectancy at birth, total (years) (SP.DYN.LE00.IN)
    # UIS: Mean years of schooling of the population age 25+. Male (UIS.EA.MEAN.1T6.AG25T99.M) - NOT AVAILABLE
    # Government expenditure on education, total (% of GDP) (SE.XPD.TOTL.GD.ZS)
    # Computer, communications and other services (% of commercial service exports) (TX.VAL.OTHR.ZS.WT)

    ids = ["NY.GDP.PCAP.PP.KD","SP.DYN.LE00.IN","NY.GNP.PCAP.PP.KD"]

    year = getRecentOfAll(ids)

    url = "http://" + request.get_host() + "/api/" + ids[0] + "/" + str(year)
    data = requests.get(url=url).json()

    return render(request, "test.html", {"data":data})

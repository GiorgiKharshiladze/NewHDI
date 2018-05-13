from django.shortcuts import render

# Create your views here.

def index(request):

	return render(request, "index.html")

def dashboard(request):

	return render(request, "dashboard.html")


# 
# ======================
# FROM DATA MINING
# 
# def validate(url): 
# #   Checks if data exists on this url
#     result = {}
#     data = requests.get(url=url).json()
#     if 'total' in data[0].keys():
#         amount = data[0]['total']
#         result['url'] = url + "&per_page=" + str(amount)
#         result['exists'] = False
#         if amount > 0 and data[1][0]['value'] != None:
#             result['exists'] = True
#     else:
#         result['exists'] = False
#     return result

# def checkList(urls, year):
# #   Helper for getRecentOfAll
#     for url in urls:
#         if not validate(url)['exists']:
#             return False
#     return True

# def getRecentOfAll(ids):
    
#     temp_year = datetime.now().year
#     end_year = temp_year - 20
    
#     while(end_year < temp_year):
#         urls = []
#         for id in ids:
#             urls.append(BASE_URL + id + "?date=" + str(temp_year) + "&format=json")

#         if checkList(urls, temp_year):
#             return temp_year
#         temp_year -= 1
        
#     return False
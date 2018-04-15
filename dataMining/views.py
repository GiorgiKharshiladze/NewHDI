from django.shortcuts import render

# Create your views here.

def api(request):
	
	result = "Giorga"

	return render(request, "index.html", {"result": result})

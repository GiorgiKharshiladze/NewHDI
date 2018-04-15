from django.conf.urls import *
from dataMining import views


urlpatterns = [
	url(r'^result/$', views.api, name='result'),
]
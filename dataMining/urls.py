from django.conf.urls import url
from django.contrib import admin
from dataMining import views


urlpatterns = [
	url(r'^result/$', views.api, name='result'),
]
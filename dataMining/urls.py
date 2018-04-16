from django.conf.urls import *
from dataMining import views


urlpatterns = [
	url(r'^result/$', views.api, name='result'),
	url(r'^fill/indicators/$', views.fill_indicators_table, name="fill_indicatos")
]
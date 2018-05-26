from dataMining import views
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
	url(r'^(?P<id>[\w\-.]+)/(?P<year>[0-9]{4})/$', views.getIndicator, name='getIndicator'),
	url(r'^(?P<id>[\w\-.]+)/(?P<year>[0-9]{4})/(?P<my_weight>[+-]?([0-9]*[.])?[0-9]+)/$', views.getValue, name='getValue'),
	url(r'^id/all/$', views.getLocalIds, name='getLocalIds'),
	url(r'^id/(?P<my_id>[\w\-.]+)/$', views.getLocal, name='getLocal'),
	# Less Important
	url(r'^result/$', views.preMine, name='result'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
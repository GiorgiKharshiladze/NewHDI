from dataMining import views
from django.conf.urls import url


urlpatterns = [
	url(r'^(?P<id>[\w\-.]+)/(?P<year>[0-9]{4})/$', views.getIndicator, name='getIndicator'),
	url(r'^(?P<id>[\w\-.]+)/(?P<year>[0-9]{4})/(?P<my_weight>[+-]?([0-9]*[.])?[0-9]+)/$', views.getValue, name='getValue'),
	url(r'^id/all/$', views.getLocalIds, name='getLocalIds'),
	url(r'^id/(?P<my_id>[\w\-.]+)/$', views.getLocal, name='getLocal'),
	# Less Important
	url(r'^result/$', views.preMine, name='result'),
	# url(r'^indicators/$', views.IndicatorList.as_view(), name='indicators'),
	# url(r'^fill/indicators/$', views.fill_indicators_table, name="fill_indicatos")
]

# urlpatterns = format_suffix_patterns(urlpatterns)
from dataMining import views
from django.conf.urls import url


urlpatterns = [
	url(r'^result/$', views.preMine, name='result'),
	url(r'^(?P<id>[\w\-.]+)/(?P<year>[0-9]{4})/$', views.getIndicator, name='getIndicator'),
	url(r'^(?P<id>[\w\-.]+)/(?P<year>[0-9]{4})/(?P<my_country>[\w]+)/$', views.getCountry, name='getCountry'),
	# url(r'^indicators/$', views.IndicatorList.as_view(), name='indicators'),
	# url(r'^fill/indicators/$', views.fill_indicators_table, name="fill_indicatos")
]

# urlpatterns = format_suffix_patterns(urlpatterns)
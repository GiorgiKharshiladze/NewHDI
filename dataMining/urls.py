from dataMining import views
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
	url(r'^result/$', views.preMine, name='result'),
	url(r'^(?P<year>[0-9]{4})/(?P<id>[\w\-.]+)/$', views.getIndicator, name='getIndicator'),
	# url(r'^indicators/$', views.IndicatorList.as_view(), name='indicators'),
	# url(r'^fill/indicators/$', views.fill_indicators_table, name="fill_indicatos")
]

urlpatterns = format_suffix_patterns(urlpatterns)
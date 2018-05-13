from dataMining import views
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
	url(r'^result/$', views.preMine, name='result'),
	
	# url(r'^indicators/$', views.IndicatorList.as_view(), name='indicators'),
	# url(r'^fill/indicators/$', views.fill_indicators_table, name="fill_indicatos")
]

urlpatterns = format_suffix_patterns(urlpatterns)
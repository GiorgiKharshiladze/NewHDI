from website import views
from django.conf.urls import url


urlpatterns = [
	# Main Routes
	url(r'^$', views.index, name='index'),
	url(r'^api_access/$', views.api_access, name='api_access'),
	url(r'^api_data_dir/$', views.api_data_dir, name='api_data_dir'),

	# Main Temporary Routes
	url(r'^test/$', views.test, name='test'),
	url(r'^customHDI/$', views.customHDI, name='customHDI'),

	# Testing Routes
	url(r'^sample/$', views.sample, name='sample'),
	url(r'^example/$', views.example, name='example'),
]
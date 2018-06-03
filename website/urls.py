from website import views
from django.conf.urls import url


urlpatterns = [
	# Main Routes
	url(r'^$', views.index, name='index'),
	url(r'^hdi/create/$', views.create_hdi, name='create_hdi'),
	url(r'^hdi/view/$', views.view_hdi, name='view_hdi'),
	# API Access
	url(r'^api/access/$', views.api_access, name='api_access'),
	url(r'^api/data_directory/$', views.api_data_dir, name='api_data_dir'),

	# Main Temporary Routes
	url(r'^test/$', views.test, name='test'),
	url(r'^customHDI/$', views.customHDI, name='customHDI'),

	# Testing Routes
	url(r'^sample/$', views.sample, name='sample'),
	url(r'^example/$', views.example, name='example'),
]
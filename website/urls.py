from website import views
from django.conf.urls import url


urlpatterns = [
	# Main Routes
	url(r'^$', views.index, name='index'),
	url(r'^customHDI/$', views.customHDI, name='customHDI'),
	url(r'^test/$', views.test, name='test'),

	# Routes for testing
	url(r'^sample/$', views.sample, name='sample'),
	url(r'^example/$', views.example, name='example'),
]
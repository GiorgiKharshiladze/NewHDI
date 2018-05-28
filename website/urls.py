from website import views
from django.conf.urls import url


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^dashboard/$', views.dashboard, name='dashboard'),
	url(r'^customHDI/$', views.customHDI, name='customHDI'),
	url(r'^test/$', views.test, name='test'),
	url(r'^example/$', views.example, name='example'),
]
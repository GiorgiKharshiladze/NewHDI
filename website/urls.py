from website import views
from django.conf.urls import url


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^dashboard/$', views.dashboard, name='dashboard'),
	url(r'^test/$', views.test, name='test'),
]
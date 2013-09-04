from django.conf.urls import patterns, url

from portfolio import views

urlpatterns = patterns('',
	url(r'^$', views.display_portfolio, name="index"),
)

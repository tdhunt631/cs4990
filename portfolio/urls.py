from django.conf.urls import patterns, url

from portfolio import views

urlpatterns = patterns('',
	url(r'^$', views.display_portfolio, name="index"),
	url(r'^(?P<study_id>\d+)/$', views.detail, name="detail"),
)

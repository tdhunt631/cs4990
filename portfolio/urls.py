from django.conf.urls import patterns, url

from portfolio import views

urlpatterns = patterns('',
#views.IndexView.as_view(), name='index')
	url(r'^$', views.display_portfolio, name="index"),
	url(r'^(?P<pk>\d+)/$', views.detail, name="detail"),
)

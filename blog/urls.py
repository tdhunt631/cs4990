from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
	url(r'^$', views.index, name="posts"),
	url(r'^(?P<url>[\w\-]+)/$', views.post, name="post"),
)

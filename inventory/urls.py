from django.conf.urls import patterns, url

from inventory import views

urlpatterns = patterns('',
	url(r'^$', views.index, name="categories"),
	url(r'^(?P<cat_id>\d+)/$', views.list, name="list"),
	url(r'^(?P<item_id>\d+)/add/$', views.addForm, name="addForm"),
	url(r'^(?P<item_id>\d+)/subtract/$', views.subtractForm, name="subtractForm"),
)

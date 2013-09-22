from django.conf.urls import patterns, url

from inventory import views

urlpatterns = patterns('',
	url(r'^$', views.index, name="categories"),
	url(r'^(?P<cat_id>\d+)/$', views.list, name="list"),
	url(r'^addCat/$', views.addCat, name="addCat"),
	url(r'^addItem/$', views.addItem, name="addItem"),
	url(r'^(?P<item_id>\d+)/addI/$', views.addI, name="addI"),
	url(r'^(?P<item_id>\d+)/subtractI/$', views.subtractI, name="subtractI"),
)

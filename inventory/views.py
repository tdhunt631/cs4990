from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from inventory.models import Category, Item
from forms import ItemForm

def index(request):
	categories = Category.objects.all()
	return render(request, 'inventory/index.html', {'categories':categories})

def list(request, cat_id):
	items = Item.objects.all().filter(category=cat_id) 
	return render(request, 'inventory/list.html', {'items': items})

def addForm(request, item_id):
	item = get_object_or_404(Item, id=item_id)
	item.quantity += 1;
	item.save()
	items = Item.objects.all().filter(category=item.category) 
	return HttpResponse(item.quantity) 

def subtractForm(request, item_id):
	item = get_object_or_404(Item, id=item_id)
	item.quantity -= 1;
	item.save()
	items = Item.objects.all().filter(category=item.category) 
	return HttpResponse(item.quantity) 


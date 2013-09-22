from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from inventory.models import Category, Item
from forms import ItemForm, CategoryForm

def index(request, message=""):
	categories = Category.objects.all()
	form = CategoryForm()
	return render(request, 'inventory/index.html', {'categories':categories, 'form':form, 'message':message})

def list(request, cat_id):
	items = Item.objects.all().filter(category=cat_id) 
	form = ItemForm()
	return render(request, 'inventory/list.html', {'items': items, 'form':form})

def addCat(request):
	if request.method == 'POST':
		form = CategoryForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			newCat = Category()
			newCat.name = cd.get('name')
			newCat.description = cd.get('description')
			newCat.save()					
			return HttpResponseRedirect('/inventory/')

	message = "Oops, it broke! You should enter in something valid."
	form = CategoryForm()
	categories = Category.objects.all()
	context = {'message': message, 'form': form, 'categories': categories, }
	return render_to_response('inventory/index.html', context, context_instance=RequestContext(request))


def addItem(request):
	if request.method == 'POST':
		form = ItemForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			newItem = Item()
			newItem.name = cd.get('name')
			newItem.description = cd.get('description')
			newItem.quantity = cd.get('quantity')
			currentCat = request.POST.get("category")
			newItem.category = get_object_or_404(Category, name=currentCat)  
			newItem.save()					
			return HttpResponseRedirect('/inventory/')

	message = "Oops, it broke! You should enter in something valid."
	form = CategoryForm()
	categories = Category.objects.all()
	context = {'message': message, 'form': form, 'categories': categories, }
	return render_to_response('inventory/index.html', context, context_instance=RequestContext(request))

def addI(request, item_id):
	item = get_object_or_404(Item, id=item_id)
	item.quantity += 1;
	item.save()
	items = Item.objects.all().filter(category=item.category) 
	return HttpResponse(item.quantity) 

def subtractI(request, item_id):
	item = get_object_or_404(Item, id=item_id)
	item.quantity -= 1;
	item.save()
	items = Item.objects.all().filter(category=item.category) 
	return HttpResponse(item.quantity) 


from django import template
from blog.models import Post, Category

register = template.Library()

@register.inclusion_tag('blog/catList.html')
def getCategories():
	catList = Category.objects.all()
	categories = []
	for cat in catList:
		categories.append(cat.title)
	return {'categories': categories}



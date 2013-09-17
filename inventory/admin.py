from django.contrib import admin
from inventory.models import Category, Item

class CategoryAdmin(admin.ModelAdmin):
	list_display =('name', 'description', 'parent',)

class ItemAdmin(admin.ModelAdmin):
	list_display=('name', 'category', 'description', 'quantity',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)

from django.contrib import admin
from blog.models import Post, Category

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'publishedDate', 'url', 'category', 'active',)
	list_filter = ['publishedDate']
	search_fields = ['title']
	date_hierarchy = 'publishedDate'

admin.site.register(Category)
admin.site.register(Post, PostAdmin)

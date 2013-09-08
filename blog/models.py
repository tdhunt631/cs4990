from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	publishedDate = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=True)
	author = models.ForeignKey(User)
	slug = models.SlugField(max_length=100, unique=True)
	category = models.ForeignKey('blog.Category')	

	def __unicode__ (self):
		return self.title

	def getUrl(self):
		return reverse('blog.views.post', args=[self.slug])

class Category(models.Model):
	title = models.CharField(max_length=100, db_index=True)
	slug = models.SlugField(max_length=100, db_index=True)
	
	def __unicode__(self):
		return self.title

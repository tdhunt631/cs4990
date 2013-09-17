from django.db import models
from django.core.urlresolvers import reverse

class Category(models.Model):
	class Meta:
		verbose_name_plural = "categories"

	name = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	parent = models.ForeignKey('self', null=True, blank=True)

	def __unicode__ (self):
		return self.name

class Item(models.Model):
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	quantity = models.IntegerField()
	category = models.ForeignKey(Category)	

	def __unicode__ (self):
		return self.name

from django.db import models
from sorl.thumbnail import ImageField

class CaseStudy(models.Model):
	class Meta:
		verbose_name_plural = "Case Studies"

	title = models.CharField(max_length=200)
	description = models.TextField()
	picture = ImageField(upload_to='photos/%Y/%m/%d')

	def __unicode__(self):
		return self.title

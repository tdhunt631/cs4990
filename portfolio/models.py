from django.db import models


class CaseStudy(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	picture =models.ImageField(upload_to="images")

	def __unicode__(self):
		return self.title

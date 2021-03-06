from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Poll(models.Model):
	author = models.CharField(max_length=60)
	question = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):
		return self.question

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date < now		

	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'	

class Choice(models.Model):
	poll = models.ForeignKey(Poll)
	answer = models.CharField(max_length=200)
	count = models.IntegerField(default=0)

	def __unicode__(self):
		return self.answer


from django import template
from portfolio.models import CaseStudy

register = template.library()

@register.simple_tag
def portfolio_images():
	img_list = CaseStudy.objects.all()
	return img_list

from django.shortcuts import render_to_response
from django.template import RequestContext
from portfolio.models import CaseStudy

def display_portfolio(request):
	casestudies = CaseStudy.objects.all()
	return render_to_response('portfolio/portfolio.html',
		{'casestudies':casestudies},
		context_instance=RequestContext(request))

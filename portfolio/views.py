from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from portfolio.models import CaseStudy
from sorl.thumbnail import ImageField

def display_portfolio(request):
	casestudies = CaseStudy.objects.all()
	return render_to_response('portfolio/portfolio.html',
		{'casestudies':casestudies},
		context_instance=RequestContext(request))

def detail(request):
	study = CaseStudy.objects.all()
	context = {'study' : study}
	return render_to_response('portfolio/detail.html', context, context_instance=RequestContext(request))

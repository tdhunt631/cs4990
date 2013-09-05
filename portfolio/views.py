from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render, get_object_or_404
from django.template import RequestContext
from portfolio.models import CaseStudy

def display_portfolio(request):
	casestudies = CaseStudy.objects.all()
	return render_to_response('portfolio/portfolio.html',
		{'casestudies':casestudies},
		context_instance=RequestContext(request))

def detail(request, study_id):
	study = get_object_or_404(CaseStudy, pk=study_id)
	context = {'study' : study}
	return render(request, 'portfolio/detail.html', context)

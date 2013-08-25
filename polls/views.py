from django.http import HttpResponse

def index(request):
	return HttpResponse("Why, hello there!  You found the index for Polls!")

def detail(request, poll_id):
	return HttpResponse("This is poll %s." % poll_id)

def results(request, poll_id):
	return HttpResponse("Yup, you found the poll results page of poll %s." % poll_id)

def vote(request, poll_id):
	return HttpResponse("This is were you vote on the poll %s." % poll_id)


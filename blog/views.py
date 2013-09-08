from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from blog.models import Post

def index(request):
	posts = Post.objects.filter(active=True)
	return render(request, 'blog/index.html', {'posts':posts})

def post(request, slug):
	post = get_object_or_404(Post, slug=slug)
	return render(request, 'blog/post.html', {'post':post})

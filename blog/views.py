from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from blog.models import Post

def index(request):
	posts = Post.objects.filter(active=True).order_by('-publishedDate')
	return render(request, 'blog/posts.html', {'posts':posts})

def post(request, url):
	post = get_object_or_404(Post, url=url)
	return render(request, 'blog/post.html', {'post':post})

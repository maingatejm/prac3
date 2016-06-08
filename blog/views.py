from django.shortcuts import render
from .model import Post

def index(request):
	post_list = Post.objects.all()
	return render(request, 'blog/index.html', {'post':post,})
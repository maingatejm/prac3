from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import CommentForm

def index(request):
	post_list = Post.objects.all()
	return render(request, 'blog/index.html', {'post_list':post_list,})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post':post,})

def comment_new(request, post_pk):
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = get_object_or_404(Post, pk=post_pk)
			comment.user = request.user
			comment = form.save()
			return redirect('blog:post_detail', post_pk)
	else : 
		form = CommentForm()
	return render(request, 'blog/comment_form.html', {'form':form,})

def comment_edit(request, post_pk, pk):
		comment = get_object_or_404(Comment, pk = pk)
		if request.method == 'POST':
			form = CommentForm(request.POST, instance=comment)
			if form.is_valid():
				comment = form.save(commit=False)
				comment.post = get_object_or_404(Post, pk=post_pk)
				comment.user = request.user
				comment.save()

			return redirect('blog:post_detail', post_pk)
		else:
			form = CommentForm(instance=comment)
		return render(request,'blog/comment_form.html', {'form':form,})
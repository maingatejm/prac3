from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'content_size', 'created_at']
	def content_size(self, post):
		return '%s자' %len(post.content)

class CommentAdmin(admin.ModelAdmin):
	list_display = ['post', 'user', 'message']


admin.site.register(Post,PostAdmin)
admin.site.register(Comment, CommentAdmin)
from django import forms
from .model import Comment

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		field = "__all__"
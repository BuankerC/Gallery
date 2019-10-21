from django import forms
from .models import Board, Comment


class BoardForm(forms.ModelForm):
    title = forms.CharField(label="오늘의 키워드")
    content = forms.CharField(label="오늘의 넋두리")

    class Meta:
        model = Board
        fields = ("title", "content",)


class CommentForm(forms.ModelForm):
    content = forms.CharField(label="댓글")

    class Meta:
        model = Comment
        fields = ("content",)

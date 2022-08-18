from django import forms
from django.core import validators
from .models import PostComment


class CommentForm(forms.ModelForm):
    comment_text = forms.CharField(widget=forms.Textarea(attrs={
        "name": "message",
        "id": "textMessage",
        "class": "form-control input-mf",
        "placeholder": "Comment *",
        "cols": "45",
        "rows": "8"
    }),
        required=True,
        validators=[validators.ProhibitNullCharactersValidator, ]
    )
    parentId = forms.IntegerField(widget=forms.HiddenInput(attrs={
        "id": "parentComment",
        "value": ""
    }),
        required=False,
    )

    class Meta:
        model = PostComment
        fields = ('comment_text',)


class SearchForm(forms.Form):
    search = forms.CharField(widget=forms.TextInput(attrs={
        "name": "search",
        "id": "search",
        "class": "form-control",
        "placeholder": "Search for...",
        "aria-label": "Search for...",
    }),
        required=True,
        validators=[validators.ProhibitNullCharactersValidator, ]
    )

    class Meta:
        fields = ('search',)
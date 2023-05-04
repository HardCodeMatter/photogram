from django import forms
from main.models import Comment


class CommentForm(forms.Form):
    comment = forms.CharField(
        max_length=300, 
        label='', 
        required=True, 
        widget=forms.Textarea(attrs={'style': 'height: 100px;'})
    )

from django import forms
from main.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image', 'title', 'description',)


class CommentForm(forms.Form):
    comment = forms.CharField(
        max_length = 300, 
        label = '', 
        required = True, 
        widget = forms.Textarea(attrs={'style': 'height: 100px;',}),
    )


class CommentUpdateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
        labels = {
            'comment': '',
        }
        widgets = {
            'comment': forms.Textarea(attrs={'style': 'height: 100px;', 'name': 'eg',}),
        }

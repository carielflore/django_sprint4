from blog.models import Post, Comment
from django import forms
from django.utils import timezone


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'pub_date', 'location', 'category', 'image']
        widgets = {'pub_date': forms.DateTimeInput(
            attrs={
                'type': 'datetime-local'
            })
        }

    def clean_pub_date(self):
        pub_date = self.cleaned_data['pub_date']
        if pub_date < timezone.now():
            raise forms.ValidationError(
                'Дата публикации не может быть в прошлом.'
            )
        return pub_date


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']

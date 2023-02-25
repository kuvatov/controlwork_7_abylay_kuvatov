from django import forms

from webapp.models import GuestBook


class GuestBookForm(forms.ModelForm):
    class Meta:
        model = GuestBook
        fields = ('author', 'email', 'text')
        labels = {
            'author': 'Имя автора',
            'email': 'Email',
            'text': 'Текст'
        }

from django import forms
from django.core.exceptions import ValidationError

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

    def clean_author(self):
        author = self.cleaned_data.get('author')
        if True in [name.isdigit() for name in author]:
            raise ValidationError('Имя не может состоять из чисел!')
        elif len(author) < 2:
            raise ValidationError('Имя не может состоять из одного символа!')
        return author.capitalize()

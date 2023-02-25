from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect

from webapp.forms import GuestBookForm
from webapp.models import GuestBook


# Create your views here.
def guest_book_view(request: WSGIRequest):
    records = GuestBook.objects.exclude(is_deleted=True)
    context = {
        'records': records
    }
    return render(request, 'home.html', context=context)


def record_add(request: WSGIRequest):
    if request.method == 'GET':
        form = GuestBookForm()
        return render(request, 'record_add.html', context={
            'form': form
        })
    form = GuestBookForm(data=request.POST)
    if form.is_valid():
        GuestBook.objects.create(**form.cleaned_data)
        return redirect('home')
    else:
        return render(request, 'record_add.html', context={
            'form': form
        })

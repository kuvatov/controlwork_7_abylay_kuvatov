from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from webapp.models import GuestBook


# Create your views here.
def guest_book_view(request: WSGIRequest):
    records = GuestBook.objects.exclude(is_deleted=True)
    context = {
        'records': records
    }
    return render(request, 'home.html', context=context)

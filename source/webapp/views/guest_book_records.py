from django.core.handlers.wsgi import WSGIRequest
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import GuestBookForm
from webapp.models import GuestBook


# Create your views here.
def guest_book_view(request: WSGIRequest):
    search_record = request.GET.get('search')
    if search_record:
        records = GuestBook.objects.filter(Q(author__icontains=search_record))
    else:
        records = GuestBook.objects.exclude(status='blocked').order_by('-created_at')
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


def record_edit(request: WSGIRequest, pk: int):
    record = get_object_or_404(GuestBook, pk=pk)
    if request.method == 'GET':
        form = GuestBookForm(instance=record)
        return render(request, 'record_edit.html', context={
            'form': form,
            'record': record
        })
    form = GuestBookForm(request.POST, instance=record)
    if form.is_valid():
        form.save()
        return redirect('home')
    else:
        return render(request, 'record_edit.html', context={
            'form': form,
            'record': record
        })


def record_delete(request: WSGIRequest, pk: int):
    record = get_object_or_404(GuestBook, pk=pk)
    record.delete()
    return redirect('home')

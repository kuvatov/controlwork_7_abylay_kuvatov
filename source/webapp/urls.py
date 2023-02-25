from django.urls import path, include

from webapp.views.guest_book_records import guest_book_view, record_add

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path("", guest_book_view, name="home"),
    path("record/add", record_add, name="record_add")
]

from django.urls import path, include

from webapp.views.guest_book_records import guest_book_view, record_add, record_edit, record_delete

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path("", guest_book_view, name="home"),
    path("record/add", record_add, name="record_add"),
    path('record/<int:pk>/edit', record_edit, name='record_edit'),
    path('record/<int:pk>/delete', record_delete, name='record_delete'),
]

from django.contrib import admin

from webapp.models import GuestBook


# Register your models here.
class GuestBookAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'email', 'text', 'status', 'created_at', 'edited_at', 'is_deleted', 'deleted_at']
    list_filter = ['author', 'email', 'status', 'created_at']
    search_fields = ['author', 'email', 'status']
    fields = ['author', 'email', 'text', 'status', 'created_at']
    list_editable = ['author', 'email', 'text', 'status', 'is_deleted']
    readonly_fields = ['created_at', 'edited_at', 'deleted_at']


admin.site.register(GuestBook, GuestBookAdmin)

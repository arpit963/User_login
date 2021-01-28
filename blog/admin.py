from django.contrib import admin
from .models import Contact, Page
# Register your models here.

@admin.register(Page)
class PageModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc']

admin.site.register(Contact)
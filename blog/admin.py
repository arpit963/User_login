from django.contrib import admin
from .models import Page
# Register your models here.

@admin.register(Page)
class PageModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc']

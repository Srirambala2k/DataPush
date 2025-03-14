from django.contrib import admin
from .models import Destination
from django.contrib.admin import ModelAdmin




class DestinationAdmin(admin.ModelAdmin):
    list_display = ['account', 'url', 'http_method', 'headers', 'created_at', 'updated_at', 'created_by', 'updated_by']
    search_fields = ['account', 'url', 'http_method', 'headers', 'created_at', 'updated_at', 'created_by', 'updated_by']




admin.site.register(Destination, DestinationAdmin)


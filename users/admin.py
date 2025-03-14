from django.contrib import admin
from .models import Role, User
from django.contrib.admin import ModelAdmin

# Register your models here.

class RoleAdmin(admin.ModelAdmin):
    list_display = ['role_name']
    search_fields = ['role_name']

class UserAdmin(admin.ModelAdmin):
    list_display = ['email','password', 'role', 'account', 'created_at']
    search_fields = ['email','password', 'role', 'account', 'created_at']

admin.site.register(Role, RoleAdmin)
admin.site.register(User, UserAdmin)

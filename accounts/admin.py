from django.contrib import admin
from .models import  Account, AccountMember
from django.contrib.admin import ModelAdmin


# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display = ['account_name', 'app_secret_token']
    search_fields = ['account_name', 'app_secret_token']

class AccountMemberAdmin(admin.ModelAdmin):
    list_display = ['account', 'user', 'role', 'created_at', 'updated_at', 'created_by', 'updated_by']
    search_fields = ['account', 'user', 'role', 'created_at', 'updated_at', 'created_by', 'updated_by']

admin.site.register(Account, AccountAdmin)
admin.site.register(AccountMember, AccountMemberAdmin)
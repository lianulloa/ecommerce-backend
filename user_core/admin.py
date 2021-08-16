from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.contrib.auth.models import User
from django.contrib import admin
from .models import *
from .adminActions import validate_users

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
  actions = [validate_users]
  list_display = ('user','phone_number','city','country','created_at','updated_at')
  list_filter = ('created_at','updated_at')
  ordering = ('-created_at',)
  date_hierarchy = 'created_at'

admin.site.unregister(User)
@admin.register(User)
class UserAdmin(DefaultUserAdmin):
  actions = [validate_users]



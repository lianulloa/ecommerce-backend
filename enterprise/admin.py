from django.contrib import admin
from .models import *

@admin.register(Enterprise)
class Enterprise(admin.ModelAdmin):
  list_display = ("name", 'description', 'url')
  ordering = ('name',)
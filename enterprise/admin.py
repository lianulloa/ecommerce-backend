from django.contrib import admin
from .models import *

@admin.register(Enterprise)
class Enterprise(admin.ModelAdmin):
  list_display = ("name", 'description', 'url')
  ordering = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  ordering = ('name',)

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
  list_display = ('name', 'category')
  ordering = ('category', 'name')
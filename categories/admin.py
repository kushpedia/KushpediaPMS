from django.contrib import admin
from .models import Category
# Register your models here.
class CategoryManager(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links =('name',)
    ordering = ('name',)


admin.site.register(Category, CategoryManager)

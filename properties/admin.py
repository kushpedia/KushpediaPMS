from django.contrib import admin
from .models import Property

# Register your models here.

class PropertyManager(admin.ModelAdmin):
    list_display = ('name','address','description','num_of_floors','num_rooms','year_built')
    list_display_links = ('name','address','description')
    ordering = ('-id',)


admin.site.register(Property,PropertyManager)

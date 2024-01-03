from django.contrib import admin
from .models import Rooms

# Register your models here.
class RoomsAdmin(admin.ModelAdmin):
    list_display = ('property', 'category', 'description', 'price')
    list_display_links = ('property', 'category', 'description')
admin.site.register(Rooms, RoomsAdmin)
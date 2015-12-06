from django.contrib import admin
from .models import Item
# Register your models here.

class ItemAdmin(admin.ModelAdmin):
	site_header = 'Monty Python administration'
	list_display = ["__unicode__", "price","quantity", "type", "updated"]

admin.site.register(Item, ItemAdmin)
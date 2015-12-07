from django.contrib import admin
from .models import Item
# Register your models here.

class ItemAdmin(admin.ModelAdmin):

	list_display = ["__unicode__", "price", "quantity", "admin_image", "type", "updated"]

readonly_fields = ('admin_image')
admin.site.register(Item, ItemAdmin)

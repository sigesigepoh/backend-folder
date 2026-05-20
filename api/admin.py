from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'contact', 'date_created')
    list_filter = ('category', 'date_created')
    search_fields = ('title', 'description', 'contact')

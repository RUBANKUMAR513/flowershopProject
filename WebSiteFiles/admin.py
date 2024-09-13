from django.contrib import admin
from .models import FlowerImage

@admin.register(FlowerImage)
class FlowerImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_date')
    search_fields = ('title',)
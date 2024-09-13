from django.contrib import admin
from .models import StoreData
# Register your models here.


@admin.register(StoreData)
class StoreDataAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email', 'phone_number', 'msg')

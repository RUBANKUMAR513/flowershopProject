from django.contrib import admin
from .models import UserDetail

# Register your models here.
@admin.register(UserDetail)
class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'phone_number', 'nation', 'district', 'state', 'taluk', 'pincode')
    search_fields = ('user__username', 'phone_number', 'nation', 'district', 'state', 'taluk', 'pincode')
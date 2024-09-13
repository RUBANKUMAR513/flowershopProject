from django.contrib import admin
from .models import Setting,ToEmail
# Register your models here.
@admin.register(Setting)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('host', 'port', 'email', 'status')
    search_fields = ('host', 'email')

    def has_add_permission(self, request):
        if Setting.objects.exists():
            return False
        return super(SettingsAdmin, self).has_add_permission(request)
    
@admin.register(ToEmail)
class ToEmailAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phonenumber', 'position', 'active_status')
    search_fields = ('name', 'email', 'phonenumber', 'position')
    list_filter = ('active_status',)
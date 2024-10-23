from django.contrib import admin
from .models import ScanRequest

@admin.register(ScanRequest)
class ScanRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'ip_list', 'status', 'result')
    search_fields = ('status',)

from django.contrib import admin
from media.models import *

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ['id', 'file_type']

@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'main_phone_number']

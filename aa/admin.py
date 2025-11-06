from django.contrib import admin

from aa.models import Avt


@admin.register(Avt)
class AvtAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')
    list_display_links = ('id', 'text')

from django.contrib import admin

from . import models


@admin.register(models.Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'description')
    ordering = ('user', '-creation_date')

@admin.register(models.ResumeItem)
class ResumeItemAdmin(admin.ModelAdmin):
    list_display = ('resume', 'title', 'company', 'start_date')
    ordering = ('resume', '-start_date')

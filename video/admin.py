from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.VideosModel)
class VideosAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'alias')
    list_editable = ('name', 'alias')


@admin.register(models.DetailModel)
class VideosAdmin(admin.ModelAdmin):
    list_display = ('id', 'alias', 'numbers', 'name')
    list_editable = ('alias', 'numbers', 'name')
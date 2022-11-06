from django.contrib import admin
from content.models import Content, Rate


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'context', 'user', 'created_at', 'updated_at')


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ('rate', 'content', 'user', 'created_at', 'updated_at')
    

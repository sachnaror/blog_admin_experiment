# Register your models here.
from django.contrib import admin

from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'timestamp')
    list_filter = ('status', 'timestamp')
    search_fields = ('title', 'content')
    ordering = ('-timestamp',)
    actions = ['publish_blogs', 'unpublish_blogs']

    def publish_blogs(self, request, queryset):
        queryset.update(status='published')
    publish_blogs.short_description = "Publish selected blogs"

    def unpublish_blogs(self, request, queryset):
        queryset.update(status='draft')
    unpublish_blogs.short_description = "Unpublish selected blogs"

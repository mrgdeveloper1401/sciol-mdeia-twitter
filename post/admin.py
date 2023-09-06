from django.contrib import admin
from .models import PostModel


@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    readonly_fields = ('update_at', )
    prepopulated_fields = {'slug': ('body', )}
    search_fields = ('user', )
    list_filter = ('create_at', 'update_at')
    raw_id_fields = ('user', )
    list_display = ('user', 'location', 'create_at', 'update_at', 'body')
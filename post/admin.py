from django.contrib import admin
from .models import PostModel


@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    ...
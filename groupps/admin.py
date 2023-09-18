from django.contrib import admin
from .models import groupss


@admin.register(groupss)
class groupsAdmin(admin.ModelAdmin):
    ...
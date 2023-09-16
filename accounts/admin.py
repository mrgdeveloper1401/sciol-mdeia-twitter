from typing import Any
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from .models import User, RelationUserModel, RecycleUser, NotificationModel
from .form import UserChangeForms, UserCreationForms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import AdminPasswordChangeForm




@admin.register(RecycleUser)
class RecycleUserAdmin(admin.ModelAdmin):
    # list_display = ['id', 'email', 'username', 'full_name', 'mobile_phone', 'is_admin', 'is_active', 'is_superuser']
    
    # def get_queryset(self, request):
    #     return RecycleUser.deleted.filter(is_delted=True)
    ...
    
@admin.register(User)
class UsersAdmin(UserAdmin):
    form = UserChangeForms
    add_form = UserCreationForms
    
    list_display = ['id', 'email', 'username', 'full_name', 'mobile_phone', 'is_admin', 'is_active', 'is_superuser']
    list_filter = ['is_admin', 'is_active', 'is_superuser']
    search_fields = ['username', 'email']
    ordering = ['username', 'create_at']
    readonly_fields = ('create_at',)
    list_display_links = ('username', 'email', 'mobile_phone')
    
    fieldsets = (
        ('authenticate', {'fields': ('email', 'password')}),
        (('persolan info'), {'fields': ('full_name','username', 'mobile_phone', 'gender_choose')}),
        (('permissions', {'fields': ('is_admin','is_superuser', 'is_active' )})),
        (('important date', {'fields': ('last_login','create_at')})),
        
        
    )
    add_fieldsets = (
        (None, {'fields': ('full_name', 'email', 'username', 'mobile_phone', 'password1', 'password2', 
                           'gender_choose')})
    ),
    
    change_password_form = AdminPasswordChangeForm
    filter_horizontal = []
    
admin.site.unregister(Group)


@admin.register(RelationUserModel)
class RelationUserAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user', 'create_at')
    

@admin.register(NotificationModel)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'body', 'create_at']
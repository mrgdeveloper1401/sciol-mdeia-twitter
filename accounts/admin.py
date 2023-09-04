from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import User
from .form import UserChangeForms, UserCreationForms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import AdminPasswordChangeForm




@admin.register(User)
class UsersAdmin(UserAdmin):
    form = UserChangeForms
    add_form = UserCreationForms
    
    list_display = ['username', 'email', 'full_name', 'mobile_phone', 'is_admin', 'is_active']
    list_filter = ['is_admin', 'is_active']
    search_fields = ['username', 'email']
    ordering = ['username', 'create_at']
    
    list_display_links = ('username', 'email', 'mobile_phone')
    
    fieldsets = (
        ('authenticate', {'fields': ('username', 'password')}),
        (('persolan info'), {'fields': ('full_name','email', 'mobile_phone', 'gender_choose')}),
        (('permissions', {'fields': ('is_admin','is_superuser', 'is_active' )})),
        (('important date', {'fields': ('update_at', 'deleted_at', 'last_login')})),
        
        
    )
    add_fieldsets = (
        (None, {'fields': ('full_name', 'email', 'username', 'mobile_phone', 'password1', 'password2', 
                           'gender_choose')})
    ),
    
    change_password_form = AdminPasswordChangeForm
    filter_horizontal = []
    
admin.site.unregister(Group)
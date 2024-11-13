from django.contrib import admin
from .models import User
from django.contrib import auth

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'is_staff', 'uuid')

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ()
        if request.user.is_staff:
            return ('is_staff', 'groups', 'user_permissions')
        return (auth.admin.UserAdmin.fields)
from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_premium', 'is_active', 'is_staff', 'date_joined')  # Fields to display in admin
    search_fields = ('username', 'email')  # Fields to search in admin
    list_filter = ('is_active', 'is_staff', 'is_premium')  # Filters to help narrow down the results

    # Optionally, add fieldsets to organize the user form in the admin
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Premium Info', {'fields': ('is_premium',)}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {'fields': ('username', 'email', 'password1', 'password2')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Premium Info', {'fields': ('is_premium',)}),
    )

    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)

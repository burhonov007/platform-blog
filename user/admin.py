from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("id", "first_name", "last_name", "nickname","email", "is_staff", "is_active", "is_moderator")
    list_filter = ("is_staff", "is_active",)
    list_display_links = ("id",)
    fieldsets = (
        ("Base", {"fields": ("email", "password", "first_name", "last_name", "nickname",)}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_moderator", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "nickname", "first_name", "last_name", "password1", "password2", "is_staff",
                "is_active", "is_moderator", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email", "first_name", "last_name",)
    ordering = ("email", "first_name",)

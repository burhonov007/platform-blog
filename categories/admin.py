from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'parent_category')
    list_filter = ('parent_category',)
    search_fields = ('name', 'description')
    ordering = ('name',)
    readonly_fields = ('parent_category',)

admin.site.register(Category, CategoryAdmin)

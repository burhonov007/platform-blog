from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator', 'publish_date', 'views', 'is_published')
    list_filter = ('category', 'is_published')
    search_fields = ('title', 'content')
    date_hierarchy = 'publish_date'
    ordering = ('-publish_date',)

admin.site.register(Post, PostAdmin)

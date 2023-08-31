from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'post', 'comment_date', 'is_approved')
    list_filter = ('is_approved',)
    search_fields = ('text', 'author__username', 'post__title')
    list_editable = ('is_approved',)
    list_per_page = 20
    ordering = ('-comment_date',)

admin.site.register(Comment, CommentAdmin)

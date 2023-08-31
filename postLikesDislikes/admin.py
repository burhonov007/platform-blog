from django.contrib import admin
from .models import PostLikesDislikes

class PostLikesDislikesAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'type', 'date')
    list_filter = ('type', 'date')
    search_fields = ('user__username', 'post__title')

admin.site.register(PostLikesDislikes, PostLikesDislikesAdmin)

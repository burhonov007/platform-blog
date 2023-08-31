from django.db import models
from django.conf import settings


class PostLikesDislikes(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey('posts.post', on_delete=models.CASCADE)
    LIKE_DISLIKE_CHOICES = (
        ('like', 'Like'),
        ('dislike', 'Dislike'),
    )
    type = models.CharField(max_length=10, choices=LIKE_DISLIKE_CHOICES)
    date = models.DateTimeField(auto_now_add=True) 

    class Meta:
        verbose_name = "PostLikesDislikes"
        verbose_name_plural = "PostLikesDislikes"
        

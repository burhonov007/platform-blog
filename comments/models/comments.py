from django.db import models
from django.conf import settings


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey('posts.post', on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        
    def __str__(self):
        return self.text
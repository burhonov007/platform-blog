from django.db import models
from django.conf import settings


class Post(models.Model):
    title = models.CharField('Title', max_length=80)
    content = models.TextField('Content', blank=True, null=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    publish_date = models.DateTimeField('Publish Date', auto_now_add=True)
    last_updated = models.DateTimeField('Last Updated', auto_now=True)
    category = models.ForeignKey('categories.category', on_delete=models.SET_NULL, null=True, related_name='posts')
    views = models.PositiveIntegerField(default=0)
    image = models.ImageField("Image", upload_to='upload/images/posts/', blank=True, null=True)
    video = models.FileField("Video", upload_to='upload/video/posts/', blank=True, null=True)
    gif = models.FileField("Gif", upload_to='upload/gif/posts/', blank=True, null=True)
    is_published = models.BooleanField('Published', default=True)



    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        
    def __str__(self):
        return self.title
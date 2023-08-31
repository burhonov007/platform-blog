from django.db import models


class Category(models.Model):
    name = models.CharField('Name',max_length=50)
    description = models.TextField('Description', blank=True, null=True)
    parent_category = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        
    def __str__(self):
        return self.name
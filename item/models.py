from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=300)
    
    class Meta:
        verbose_name_plural = 'categories'
        
    def __str__(self):
        return self.name
    
class Item(models.Model):
    title = models.CharField(max_length=300)
    category = models.ForeignKey(Category, related_name='item', on_delete= models.CASCADE)
    details = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    video = models.FileField(upload_to= 'files', blank=True, null=True)
    cover = models.ImageField(upload_to= 'cover_image', blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='Item', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
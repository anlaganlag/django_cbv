from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="images")
    title = models.CharField(max_length=300)
    url = models.URLField()

    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True, db_index=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    
    def __str__(self): 
        return self.title
        
    def save(self, *args, **kwargs):
        super(Image, self).save(*args, **kwargs)
# Create your models here.
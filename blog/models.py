from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
import os

class Post(models.Model):
    title=models.CharField(max_length=100,blank=True)
    content=models.TextField(blank=True)
    Date=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    image=models.ImageField(default="",blank=True,upload_to='post_images')

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args,**kwargs)

    def save(self, *args, **kwargs):
        super().save()
        try :
            img=Image.open(self.image.path)
            if img.height > 1024 or img.width > 1024:
                new_img = (1024,1024)
                img.thumbnail(new_img)
                img.save(self.image.path)
        except:
            pass
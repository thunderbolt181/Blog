from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.shortcuts import redirect

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address=models.CharField(max_length=200)
    dob=models.DateField(blank=True, null=True)
    image = models.ImageField(default="default.jpg", upload_to='profile_pics')

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save()
        img=Image.open(self.image.path)
        if img.height > 1024 or img.width > 1024:
            new_img = (1024,1024)
            img.thumbnail(new_img)
            img.save(self.image.path)

from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True)
    country = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=255, blank=True)
    # avatar = models.ImageField(upload_to='profile_avatars')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    # # The save method is no longer needed since we're not handling image resizing here.
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)  # Call the "real" save() method.
    #     img = Image.open(self.avatar.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.avatar.path)
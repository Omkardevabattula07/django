from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Userprofile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.TextField(blank=False)
    profile_pic=models.ImageField(upload_to='profile_pics/',default='asta.jpeg')
    is_approved=models.BooleanField(default=False)
    def __str__(self):
        return self.user.username
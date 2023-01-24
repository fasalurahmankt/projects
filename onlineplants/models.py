import profile

from django.db import models
import os
# Create your models here.
class details(models.Model):
    name=models.CharField(max_length=100 )
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    image=models.ImageField(upload_to="profile")

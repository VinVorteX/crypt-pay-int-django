from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Creator(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/creators/', blank=True, null=True)
    user = models.OneToOneField(User, related_name='creator', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


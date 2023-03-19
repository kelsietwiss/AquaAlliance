from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class DocModel(models.Model):
    doc = models.FileField(upload_to='images/')
    title = models.TextField(max_length=128, null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    author = User

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    Video_file = models.FileField(upload_to='videos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
    
    
class Blog(models.Model):
    title = models.CharField(max_length=200)
    blogger = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_posted']
    

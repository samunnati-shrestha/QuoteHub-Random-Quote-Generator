from django.db import models

# Create your models here.
class Quote(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=50, blank=True, default="Unknown")
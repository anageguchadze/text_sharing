from django.db import models

# Create your models here.
class Text(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
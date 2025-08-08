# Create your models here.
from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField(blank=True, null=True)
    source = models.CharField(max_length=255)
    published_at = models.DateTimeField()

    def __str__(self):
        return self.title
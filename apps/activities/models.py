from django.db import models
from django.utils import timezone


class Activity(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    description = models.TextField()

    def __str__(self):
        return self.title

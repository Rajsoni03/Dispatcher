from django.db import models


# Create your models here.
class Board(models.Model):
    name = models.CharField(blank=True, max_length=200)
    capability = models.CharField(blank=True, max_length=500)
    host_tee = models.CharField(blank=True, max_length=100)
    is_alive = models.BooleanField(default=False)
    is_free = models.BooleanField(default=False)
    last_used = models.DateTimeField(blank=True)
    added_at = models.DateTimeField(blank=True)

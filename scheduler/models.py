from django.db import models
from test_utils.models import TestCase


# Create your models here.
class Job(models.Model):
    job_name = models.CharField(blank=True, max_length=200)
    test_cases = models.ManyToManyField(TestCase, blank=True)
    started_at = models.DateTimeField(blank=True)
    end_at = models.DateTimeField(blank=True)


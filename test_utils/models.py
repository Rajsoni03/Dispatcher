from django.db import models


# Create your models here.
class TestCase(models.Model):
    name = models.CharField(blank=True, max_length=100)
    jira_id = models.CharField(blank=True, max_length=100)
    request_json = models.TextField(blank=True)
    result_json = models.TextField(blank=True)
    is_done = models.BooleanField(default=False)
    datetime = models.DateTimeField(blank=True)

    def __str__(self):
        return f'{self.name} ({self.jira_id})'

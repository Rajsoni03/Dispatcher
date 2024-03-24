from django.contrib import admin
from .models import TestCase


# Register your models here.
@admin.register(TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    list_display = ["id", "is_done", "name", "jira_id", "request_json", "result_json", "datetime"]
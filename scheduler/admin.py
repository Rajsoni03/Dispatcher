from django.contrib import admin
from .models import Job


# Register your models here.
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ["id", "job_name", "started_at", "end_at"]

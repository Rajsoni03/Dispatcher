from django.contrib import admin
from .models import Board


# Register your models here.
@admin.register(Board)
class BoardsAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "is_alive", "is_free", "capability", "host_tee", "last_used", "added_at"]

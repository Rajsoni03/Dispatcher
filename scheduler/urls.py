from . import views
from django.urls import path


urlpatterns = [
    path('schedule_job', views.schedule_job),
]
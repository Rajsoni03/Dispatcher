from . import views
from django.urls import path

urlpatterns = [
    path('get_boards_list', views.get_boards_list, name="get_boards_list")
]
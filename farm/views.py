from django.http import JsonResponse
from django.shortcuts import render
from .models import Board


# Create your views here.
def get_boards_list(request):
    data = {
        "boards": []
    }

    for obj in Board.objects.all():
        data['boards'].append({
            'id': obj.id,
            'name': obj.name,
            'host_tee': obj.host_tee,
            'capability': obj.capability,
            'is_free': obj.is_free,
        })
    return JsonResponse(data=data)

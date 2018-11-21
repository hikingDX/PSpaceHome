# chat/views.py
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

from app.chat.task import mytask


def index(request):
    return render(request, 'chat/index.html', {})


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })


def taskfinish(request):
    if request.method == 'GET':
        mytask()
        return JsonResponse({'code': 101, 'message': '无效请求'})
    else:
        token = request.POST.get('token')
        if token != '1001':
            return JsonResponse({'code': 101, 'message': '无效请求'})
        mytask()
    return JsonResponse({'code': 100, 'message': '已通知'})

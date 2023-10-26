from django.shortcuts import render
from django.http import JsonResponse
from .models import Messages


def chat_page(request, *args, **kwargs):
    context = {}
    return render(request, "chat.html", context)


def get_last_messages(request, count=100):
    messages = Messages.objects.order_by('created_at')[:count]
    message_data = [
        {'author': message.author.username,
         'message': message.text,
         'created_at': message.created_at}
        for message in messages
    ]
    return JsonResponse({'messages': message_data})

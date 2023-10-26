from django.urls import path
from chat.chat_service import ChatService
 

websocket_urlpatterns = [
    path("" , ChatService.as_asgi()) , 
]

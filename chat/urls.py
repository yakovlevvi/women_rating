from django.urls import path
from chat import views as chat_views
 
 
urlpatterns = [
    path("", chat_views.chat_page, name="chat"),
    path('get_last_messages', chat_views.get_last_messages, name='get_last_messages'),
]

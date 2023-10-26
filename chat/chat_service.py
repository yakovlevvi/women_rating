import json
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from .models import Messages
from scores.models import TopUser
 

class ChatService(AsyncWebsocketConsumer):

    async def connect(self):
        self.chat_box_name = 'home'
        self.group_name = "home_group"

        await self.channel_layer.group_add(self.group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        return super().disconnect(close_code)

    @sync_to_async
    def save_message(self, user_id: int, message: str) -> TopUser:
        user_instance = TopUser.objects.get(id=user_id)
        Messages.objects.create(
            author=user_instance,
            text=message
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        user_id = text_data_json["user_id"]
        message = text_data_json["message"]
        username = text_data_json["username"]
        
        await self.save_message(user_id, message)

        await self.channel_layer.group_send(
            self.group_name,{
                "type" : "send_message" ,
                "message" : message , 
                "username" : username ,
            })
    
    async def send_message(self, event):
        message = event["message"]
        username = event["username"]
        await self.send(text_data = json.dumps({"message":message ,"username":username}))

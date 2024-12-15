from channels.generic.websocket import AsyncWebsocketConsumer
import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class CartConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]
        self.group_name = f"cart_{self.user.id}"

        # Присоединяемся к группе
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Отключаемся от группы
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    # Получение сообщений из WebSocket
    async def receive(self, text_data):
        data = json.loads(text_data)
        action = data.get("action")

        if action == "update_cart":
            await self.channel_layer.group_send(
                self.group_name,
                {
                    "type": "cart_update",
                    "message": "Cart updated successfully!"
                }
            )

    # Отправка сообщений в WebSocket
    async def cart_update(self, event):
        message = event["message"]

        await self.send(text_data=json.dumps({
            "message": message
        }))

# Функция для отправки обновления корзины всем подключённым пользователям
def send_cart_update(user):
    channel_layer = get_channel_layer()
    group_name = f"cart_{user.id}"

    # Отправляем сообщение в группу
    async_to_sync(channel_layer.group_send)(
        group_name,
        {
            "type": "cart_update",
            "message": "Cart updated successfully!"
        }
    )

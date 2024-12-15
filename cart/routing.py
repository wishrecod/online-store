from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/cart/', consumers.CartConsumer.as_asgi()),
]
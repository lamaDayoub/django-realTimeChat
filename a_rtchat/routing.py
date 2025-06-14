from django.urls import path 
from .consumers import *

websocket_urlpatterns=[
    path("ws/chatroom/<chatroom_name>",ChatroomConsumer.as_asgi()),
    path("ws/online-status/",OnlineStatusConsumer.as_asgi()),
    path("chat/room/ws/online-status/", OnlineStatusConsumer.as_asgi()),
    path("chat/new_groupchat/ws/online-status/", OnlineStatusConsumer.as_asgi()),
]
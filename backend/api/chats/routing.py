from django.urls import path, re_path

from .consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r"^ws/chat/(?P<username1>[\w@.:+-]+)/(?P<username2>[\w@.-]+)/$", ChatConsumer.as_asgi())
]

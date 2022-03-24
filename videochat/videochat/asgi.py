"""
ASGI config for videochat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
import channels
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator

from django.urls import path, include

from video.consumers import VideoChat


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'videochat.settings')

application = ProtocolTypeRouter({
    'websocket': AllowedHostsOriginValidator(
        URLRouter([
            path('ws/', VideoChat.as_asgi()),
        ])
    )
})

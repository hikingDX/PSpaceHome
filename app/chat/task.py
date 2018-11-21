# 在任务处理者端加这几句
# import os
# import django

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PSpaceHome.settings')
# django.setup()

import channels.layers

channel_layer = channels.layers.get_channel_layer()
from asgiref.sync import async_to_sync


def mytask():
    async_to_sync(channel_layer.group_send)(
        'chat_hiking',
        {
            'type': 'chat_message',
            'message': '1'
        }
    )

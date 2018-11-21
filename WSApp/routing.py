# In routing.py
from channels.routing import route_pattern_match
from WSApp.consumers import ws_message

channel_routing = [
    route_pattern_match("websocket.receive", ws_message),
]

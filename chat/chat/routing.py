channel_routing = {
    "websocket.connect": "chatroom.consumers.ws_add",
    "websocket.keepalive": "chatroom.consumers.ws_keepalive",
    "websocket.receive": "chatroom.consumers.ws_message",
    "websocket.disconnect": "chatroom.consumers.ws_disconnect",
}

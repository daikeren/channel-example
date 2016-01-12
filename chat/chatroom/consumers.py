from channels import Group
from channels.decorators import channel_session, linearize


@linearize
@channel_session
def ws_add(message):
    room = message.content.get('path').strip('/')
    message.channel_session['room'] = room
    print "Room: {room} - ws_add".format(room=room)
    Group("chat-%s" % room).add(
        message.reply_channel
    )


@channel_session
def ws_keepalive(message):
    room = message.channel_session['room']
    Group("chat-%s" % room).add(
        message.reply_channel
    )


@channel_session
def ws_disconnect(message):
    Group("chat-%s" % message.channel_session['room']).discard(
        message.reply_channel
    )


@linearize
@channel_session
def ws_message(message):
    Group("chat-%s" % message.channel_session['room']).send(
        content=message.content
    )

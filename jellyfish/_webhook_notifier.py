"""
Module defining a function allowing decoding received webhook 
notification from jellyfish to notification structs.
"""

import betterproto

from jellyfish.events._protos.jellyfish import ServerMessage


def receive_binary(binary: bytes) -> betterproto.Message:
    """
    Transform received protobuf notification to adequate notification instance.

    The available notifications are listed in `jellyfish.events` module.
    """
    message = ServerMessage().parse(binary)
    _which, message = betterproto.which_one_of(message, "content")
    return message

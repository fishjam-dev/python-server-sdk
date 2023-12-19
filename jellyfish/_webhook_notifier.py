"""
Module defining a function allowing decoding received webhook 
notification from jellyfish to notification structs.
"""

from typing import Dict

import betterproto

from jellyfish.events._protos.jellyfish import ServerMessage


def receive_json(json: Dict) -> betterproto.Message:
    """
    Transform received json notification to adequate notification instance.

    The available notifications are listed in `jellyfish.events` module.
    """
    msg = json["notification"]
    msg = bytes(msg, "utf-8")
    message = ServerMessage().parse(msg)
    _which, message = betterproto.which_one_of(message, "content")
    return message

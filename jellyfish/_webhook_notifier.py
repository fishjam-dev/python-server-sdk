"""
Module defining a function allowing decoding received webhook 
notification from jellyfish to notification structs.
"""

import inspect
from typing import Dict, Union

import betterproto

import jellyfish
from jellyfish.events._protos.jellyfish import ServerMessage

SERVER_MESSAGE_TYPES = tuple(m[0] for m in inspect.getmembers(jellyfish.events, inspect.isclass))


def receive_json(json: Dict) -> Union[SERVER_MESSAGE_TYPES]:
    """
    Transform received json notification to adequate notification instance.

    The available notifications are listed in `jellyfish.events` module.
    """
    msg = json["notification"]
    msg = bytes(msg, "utf-8")
    message = ServerMessage().parse(msg)
    _which, message = betterproto.which_one_of(message, "content")
    return message

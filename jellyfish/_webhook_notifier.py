"""
Module defining a function allowing decoding received webhook notification from jellyfish to notification structs.
"""

from typing import Any, Dict

import betterproto

from jellyfish.events import  ServerMessage



def receive_json(json: Dict) -> Any:
        """
        Transform received json notification to adequate notification instance.
        """
        msg = json["notification"]
        msg = bytes(msg, "utf-8")
        message = ServerMessage().parse(msg)
        _which, message = betterproto.which_one_of(message, "content")
        return message

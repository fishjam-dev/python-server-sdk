from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.room_config_video_codec import RoomConfigVideoCodec
from ..types import UNSET, Unset

T = TypeVar("T", bound="RoomConfig")


@_attrs_define
class RoomConfig:
    """Room configuration"""

    max_peers: Union[Unset, None, int] = UNSET
    """Maximum amount of peers allowed into the room"""
    peer_disconnected_timeout: Union[Unset, None, int] = UNSET
    """Duration (in seconds) after which the peer will be removed if it is disconnected. If not provided, this feature is disabled."""
    peerless_purge_timeout: Union[Unset, None, int] = UNSET
    """Duration (in seconds) after which the room will be removed if no peers are connected. If not provided, this feature is disabled."""
    room_id: Union[Unset, None, str] = UNSET
    """Custom id used for identifying room within Fishjam. Must be unique across all rooms. If not provided, random UUID is generated."""
    video_codec: Union[Unset, None, RoomConfigVideoCodec] = UNSET
    """Enforces video codec for each peer in the room"""
    webhook_url: Union[Unset, None, str] = UNSET
    """URL where Fishjam notifications will be sent"""
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)
    """@private"""

    def to_dict(self) -> Dict[str, Any]:
        """@private"""
        max_peers = self.max_peers
        peer_disconnected_timeout = self.peer_disconnected_timeout
        peerless_purge_timeout = self.peerless_purge_timeout
        room_id = self.room_id
        video_codec: Union[Unset, None, str] = UNSET
        if not isinstance(self.video_codec, Unset):
            video_codec = self.video_codec.value if self.video_codec else None

        webhook_url = self.webhook_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_peers is not UNSET:
            field_dict["maxPeers"] = max_peers
        if peer_disconnected_timeout is not UNSET:
            field_dict["peerDisconnectedTimeout"] = peer_disconnected_timeout
        if peerless_purge_timeout is not UNSET:
            field_dict["peerlessPurgeTimeout"] = peerless_purge_timeout
        if room_id is not UNSET:
            field_dict["roomId"] = room_id
        if video_codec is not UNSET:
            field_dict["videoCodec"] = video_codec
        if webhook_url is not UNSET:
            field_dict["webhookUrl"] = webhook_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        """@private"""
        d = src_dict.copy()
        max_peers = d.pop("maxPeers", UNSET)

        peer_disconnected_timeout = d.pop("peerDisconnectedTimeout", UNSET)

        peerless_purge_timeout = d.pop("peerlessPurgeTimeout", UNSET)

        room_id = d.pop("roomId", UNSET)

        _video_codec = d.pop("videoCodec", UNSET)
        video_codec: Union[Unset, None, RoomConfigVideoCodec]
        if _video_codec is None:
            video_codec = None
        elif isinstance(_video_codec, Unset):
            video_codec = UNSET
        else:
            video_codec = RoomConfigVideoCodec(_video_codec)

        webhook_url = d.pop("webhookUrl", UNSET)

        room_config = cls(
            max_peers=max_peers,
            peer_disconnected_timeout=peer_disconnected_timeout,
            peerless_purge_timeout=peerless_purge_timeout,
            room_id=room_id,
            video_codec=video_codec,
            webhook_url=webhook_url,
        )

        room_config.additional_properties = d
        return room_config

    @property
    def additional_keys(self) -> List[str]:
        """@private"""
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

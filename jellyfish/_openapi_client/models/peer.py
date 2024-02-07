from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.peer_status import PeerStatus

if TYPE_CHECKING:
    from ..models.track import Track


T = TypeVar("T", bound="Peer")


@_attrs_define
class Peer:
    """Describes peer status"""

    id: str
    """Assigned peer id"""
    metadata: Any
    """Custom metadata set by the peer"""
    status: PeerStatus
    """Informs about the peer status"""
    tracks: List["Track"]
    """List of all peer's tracks"""
    type: str
    """Peer type"""
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)
    """@private"""

    def to_dict(self) -> Dict[str, Any]:
        """@private"""
        id = self.id
        metadata = self.metadata
        status = self.status.value

        tracks = []
        for tracks_item_data in self.tracks:
            tracks_item = tracks_item_data.to_dict()

            tracks.append(tracks_item)

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "metadata": metadata,
                "status": status,
                "tracks": tracks,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        """@private"""
        from ..models.track import Track

        d = src_dict.copy()
        id = d.pop("id")

        metadata = d.pop("metadata")

        status = PeerStatus(d.pop("status"))

        tracks = []
        _tracks = d.pop("tracks")
        for tracks_item_data in _tracks:
            tracks_item = Track.from_dict(tracks_item_data)

            tracks.append(tracks_item)

        type = d.pop("type")

        peer = cls(
            id=id,
            metadata=metadata,
            status=status,
            tracks=tracks,
            type=type,
        )

        peer.additional_properties = d
        return peer

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

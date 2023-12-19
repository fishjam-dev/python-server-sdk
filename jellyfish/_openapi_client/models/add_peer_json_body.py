from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.peer_options_web_rtc import PeerOptionsWebRTC


T = TypeVar("T", bound="AddPeerJsonBody")


@_attrs_define
class AddPeerJsonBody:
    """ """

    options: "PeerOptionsWebRTC"
    """Options specific to the WebRTC peer"""
    type: str
    """Peer type"""
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)
    """@private"""

    def to_dict(self) -> Dict[str, Any]:
        """@private"""
        options = self.options.to_dict()

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "options": options,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        """@private"""
        from ..models.peer_options_web_rtc import PeerOptionsWebRTC

        d = src_dict.copy()
        options = PeerOptionsWebRTC.from_dict(d.pop("options"))

        type = d.pop("type")

        add_peer_json_body = cls(
            options=options,
            type=type,
        )

        add_peer_json_body.additional_properties = d
        return add_peer_json_body

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

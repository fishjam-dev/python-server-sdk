from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.room import Room


T = TypeVar("T", bound="RoomCreateDetailsResponseData")


@_attrs_define
class RoomCreateDetailsResponseData:
    """ """

    fishjam_address: str
    """Fishjam instance address where the room was created. This might be different than the address of Fishjam where the request was sent only when running a cluster of Fishjams."""
    room: "Room"
    """Description of the room state"""
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)
    """@private"""

    def to_dict(self) -> Dict[str, Any]:
        """@private"""
        fishjam_address = self.fishjam_address
        room = self.room.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fishjam_address": fishjam_address,
                "room": room,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        """@private"""
        from ..models.room import Room

        d = src_dict.copy()
        fishjam_address = d.pop("fishjam_address")

        room = Room.from_dict(d.pop("room"))

        room_create_details_response_data = cls(
            fishjam_address=fishjam_address,
            room=room,
        )

        room_create_details_response_data.additional_properties = d
        return room_create_details_response_data

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

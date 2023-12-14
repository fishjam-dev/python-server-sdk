from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.room_create_details_response_data import RoomCreateDetailsResponseData


T = TypeVar("T", bound="RoomCreateDetailsResponse")


@_attrs_define
class RoomCreateDetailsResponse:
    """Response containing room details"""

    data: "RoomCreateDetailsResponseData"
    """"""
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)
    """@private"""

    def to_dict(self) -> Dict[str, Any]:
        """@private"""
        data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        """@private"""
        from ..models.room_create_details_response_data import RoomCreateDetailsResponseData

        d = src_dict.copy()
        data = RoomCreateDetailsResponseData.from_dict(d.pop("data"))

        room_create_details_response = cls(
            data=data,
        )

        room_create_details_response.additional_properties = d
        return room_create_details_response

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

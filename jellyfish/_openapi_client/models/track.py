from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.track_type import TrackType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Track")


@_attrs_define
class Track:
    """Describes media track of a Peer or Component"""

    id: Union[Unset, str] = UNSET
    """None"""
    metadata: Union[Unset, Any] = UNSET
    """None"""
    type: Union[Unset, TrackType] = UNSET
    """None"""
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)
    """@private"""

    def to_dict(self) -> Dict[str, Any]:
        """@private"""
        id = self.id
        metadata = self.metadata
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        """@private"""
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        metadata = d.pop("metadata", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, TrackType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = TrackType(_type)

        track = cls(
            id=id,
            metadata=metadata,
            type=type,
        )

        track.additional_properties = d
        return track

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

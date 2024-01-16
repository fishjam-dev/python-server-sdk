from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.component_properties_file import ComponentPropertiesFile
    from ..models.track import Track


T = TypeVar("T", bound="ComponentFile")


@_attrs_define
class ComponentFile:
    """Describes the File component"""

    id: str
    """Assigned component ID"""
    tracks: List["Track"]
    """List of all component's tracks"""
    type: str
    """Component type"""
    properties: Union[Unset, "ComponentPropertiesFile"] = UNSET
    """Properties specific to the File component"""
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)
    """@private"""

    def to_dict(self) -> Dict[str, Any]:
        """@private"""
        id = self.id
        tracks = []
        for tracks_item_data in self.tracks:
            tracks_item = tracks_item_data.to_dict()

            tracks.append(tracks_item)

        type = self.type
        properties: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "tracks": tracks,
                "type": type,
            }
        )
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        """@private"""
        from ..models.component_properties_file import ComponentPropertiesFile
        from ..models.track import Track

        d = src_dict.copy()
        id = d.pop("id")

        tracks = []
        _tracks = d.pop("tracks")
        for tracks_item_data in _tracks:
            tracks_item = Track.from_dict(tracks_item_data)

            tracks.append(tracks_item)

        type = d.pop("type")

        _properties = d.pop("properties", UNSET)
        properties: Union[Unset, ComponentPropertiesFile]
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = ComponentPropertiesFile.from_dict(_properties)

        component_file = cls(
            id=id,
            tracks=tracks,
            type=type,
            properties=properties,
        )

        component_file.additional_properties = d
        return component_file

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

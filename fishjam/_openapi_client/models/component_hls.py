from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.component_properties_hls import ComponentPropertiesHLS
    from ..models.track import Track


T = TypeVar("T", bound="ComponentHLS")


@_attrs_define
class ComponentHLS:
    """Describes the HLS component"""

    id: str
    """Assigned component ID"""
    properties: "ComponentPropertiesHLS"
    """Properties specific to the HLS component"""
    tracks: List["Track"]
    """List of all component's tracks"""
    type: str
    """Component type"""
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)
    """@private"""

    def to_dict(self) -> Dict[str, Any]:
        """@private"""
        id = self.id
        properties = self.properties.to_dict()

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
                "properties": properties,
                "tracks": tracks,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        """@private"""
        from ..models.component_properties_hls import ComponentPropertiesHLS
        from ..models.track import Track

        d = src_dict.copy()
        id = d.pop("id")

        properties = ComponentPropertiesHLS.from_dict(d.pop("properties"))

        tracks = []
        _tracks = d.pop("tracks")
        for tracks_item_data in _tracks:
            tracks_item = Track.from_dict(tracks_item_data)

            tracks.append(tracks_item)

        type = d.pop("type")

        component_hls = cls(
            id=id,
            properties=properties,
            tracks=tracks,
            type=type,
        )

        component_hls.additional_properties = d
        return component_hls

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

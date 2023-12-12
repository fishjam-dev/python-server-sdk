from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.component_properties_hls import ComponentPropertiesHLS


T = TypeVar("T", bound="ComponentHLS")


@_attrs_define
class ComponentHLS:
    """Describes the HLS component

    Attributes:
        id (str): Assigned component ID Example: component-1.
        properties (ComponentPropertiesHLS): Properties specific to the HLS component
        type (str): Component type Example: hls.
    """

    id: str
    properties: "ComponentPropertiesHLS"
    type: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        properties = self.properties.to_dict()

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "properties": properties,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.component_properties_hls import ComponentPropertiesHLS

        d = src_dict.copy()
        id = d.pop("id")

        properties = ComponentPropertiesHLS.from_dict(d.pop("properties"))

        type = d.pop("type")

        component_hls = cls(
            id=id,
            properties=properties,
            type=type,
        )

        component_hls.additional_properties = d
        return component_hls

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.component_properties_sip import ComponentPropertiesSIP


T = TypeVar("T", bound="ComponentSIP")


@_attrs_define
class ComponentSIP:
    """Describes the SIP component"""

    id: str
    """Assigned component ID"""
    type: str
    """Component type"""
    properties: Union[Unset, "ComponentPropertiesSIP"] = UNSET
    """Properties specific to the SIP component"""
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)
    """@private"""

    def to_dict(self) -> Dict[str, Any]:
        """@private"""
        id = self.id
        type = self.type
        properties: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type,
            }
        )
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        """@private"""
        from ..models.component_properties_sip import ComponentPropertiesSIP

        d = src_dict.copy()
        id = d.pop("id")

        type = d.pop("type")

        _properties = d.pop("properties", UNSET)
        properties: Union[Unset, ComponentPropertiesSIP]
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = ComponentPropertiesSIP.from_dict(_properties)

        component_sip = cls(
            id=id,
            type=type,
            properties=properties,
        )

        component_sip.additional_properties = d
        return component_sip

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

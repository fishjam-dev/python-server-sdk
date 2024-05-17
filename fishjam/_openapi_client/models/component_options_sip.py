from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.component_options_sipsip_credentials import (
        ComponentOptionsSIPSIPCredentials,
    )


T = TypeVar("T", bound="ComponentOptionsSIP")


@_attrs_define
class ComponentOptionsSIP:
    """Options specific to the SIP component"""

    registrar_credentials: "ComponentOptionsSIPSIPCredentials"
    """Credentials used to authorize in SIP Provider service"""
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)
    """@private"""

    def to_dict(self) -> Dict[str, Any]:
        """@private"""
        registrar_credentials = self.registrar_credentials.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "registrarCredentials": registrar_credentials,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        """@private"""
        from ..models.component_options_sipsip_credentials import (
            ComponentOptionsSIPSIPCredentials,
        )

        d = src_dict.copy()
        registrar_credentials = ComponentOptionsSIPSIPCredentials.from_dict(
            d.pop("registrarCredentials")
        )

        component_options_sip = cls(
            registrar_credentials=registrar_credentials,
        )

        component_options_sip.additional_properties = d
        return component_options_sip

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

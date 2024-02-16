from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ComponentPropertiesSIPSIPCredentials")


@_attrs_define
class ComponentPropertiesSIPSIPCredentials:
    """Credentials used to authorize in SIP Provider service"""

    address: str
    """SIP provider address. Can be in the form of FQDN (my-sip-registrar.net) or IPv4 (1.2.3.4). Port can be specified e.g: 5.6.7.8:9999. If not given, the default SIP port `5060` will be assumed"""
    password: str
    """Password in SIP service provider"""
    username: str
    """Username in SIP service provider"""
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)
    """@private"""

    def to_dict(self) -> Dict[str, Any]:
        """@private"""
        address = self.address
        password = self.password
        username = self.username

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "address": address,
                "password": password,
                "username": username,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        """@private"""
        d = src_dict.copy()
        address = d.pop("address")

        password = d.pop("password")

        username = d.pop("username")

        component_properties_sipsip_credentials = cls(
            address=address,
            password=password,
            username=username,
        )

        component_properties_sipsip_credentials.additional_properties = d
        return component_properties_sipsip_credentials

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

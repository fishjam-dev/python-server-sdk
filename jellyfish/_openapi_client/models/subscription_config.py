from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscriptionConfig")


@_attrs_define
class SubscriptionConfig:
    """Subscription config"""

    origins: Union[Unset, List[str]] = UNSET
    """List of peers and components ids whose tracks the HLS endpoint will subscribe to"""
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)
    """@private"""

    def to_dict(self) -> Dict[str, Any]:
        """@private"""
        origins: Union[Unset, List[str]] = UNSET
        if not isinstance(self.origins, Unset):
            origins = self.origins

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if origins is not UNSET:
            field_dict["origins"] = origins

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        """@private"""
        d = src_dict.copy()
        origins = cast(List[str], d.pop("origins", UNSET))

        subscription_config = cls(
            origins=origins,
        )

        subscription_config.additional_properties = d
        return subscription_config

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

from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscriptionConfig")


@_attrs_define
class SubscriptionConfig:
    """Subscription config

    Attributes:
        tracks (Union[Unset, List[str]]): List of tracks that hls endpoint will subscribe for
    """

    tracks: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tracks: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tracks, Unset):
            tracks = self.tracks

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tracks is not UNSET:
            field_dict["tracks"] = tracks

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tracks = cast(List[str], d.pop("tracks", UNSET))

        subscription_config = cls(
            tracks=tracks,
        )

        subscription_config.additional_properties = d
        return subscription_config

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

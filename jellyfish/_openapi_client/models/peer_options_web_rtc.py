from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PeerOptionsWebRTC")


@_attrs_define
class PeerOptionsWebRTC:
    """Options specific to the WebRTC peer

    Attributes:
        enable_simulcast (Union[Unset, bool]): Enables the peer to use simulcast Default: True.
    """

    enable_simulcast: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enable_simulcast = self.enable_simulcast

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable_simulcast is not UNSET:
            field_dict["enableSimulcast"] = enable_simulcast

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enable_simulcast = d.pop("enableSimulcast", UNSET)

        peer_options_web_rtc = cls(
            enable_simulcast=enable_simulcast,
        )

        peer_options_web_rtc.additional_properties = d
        return peer_options_web_rtc

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

from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ComponentOptionsRTSP")


@_attrs_define
class ComponentOptionsRTSP:
    """Options specific to the RTSP component"""

    source_uri: str
    """URI of RTSP source stream"""
    keep_alive_interval: Union[Unset, int] = 15000
    """Interval (in ms) in which keep-alive RTSP messages will be sent to the remote stream source"""
    pierce_nat: Union[Unset, bool] = True
    """Whether to attempt to create client-side NAT binding by sending an empty datagram from client to source, after the completion of RTSP setup"""
    reconnect_delay: Union[Unset, int] = 15000
    """Delay (in ms) between successive reconnect attempts"""
    rtp_port: Union[Unset, int] = 20000
    """Local port RTP stream will be received at"""
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)
    """@private"""

    def to_dict(self) -> Dict[str, Any]:
        """@private"""
        source_uri = self.source_uri
        keep_alive_interval = self.keep_alive_interval
        pierce_nat = self.pierce_nat
        reconnect_delay = self.reconnect_delay
        rtp_port = self.rtp_port

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sourceUri": source_uri,
            }
        )
        if keep_alive_interval is not UNSET:
            field_dict["keepAliveInterval"] = keep_alive_interval
        if pierce_nat is not UNSET:
            field_dict["pierceNat"] = pierce_nat
        if reconnect_delay is not UNSET:
            field_dict["reconnectDelay"] = reconnect_delay
        if rtp_port is not UNSET:
            field_dict["rtpPort"] = rtp_port

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        """@private"""
        d = src_dict.copy()
        source_uri = d.pop("sourceUri")

        keep_alive_interval = d.pop("keepAliveInterval", UNSET)

        pierce_nat = d.pop("pierceNat", UNSET)

        reconnect_delay = d.pop("reconnectDelay", UNSET)

        rtp_port = d.pop("rtpPort", UNSET)

        component_options_rtsp = cls(
            source_uri=source_uri,
            keep_alive_interval=keep_alive_interval,
            pierce_nat=pierce_nat,
            reconnect_delay=reconnect_delay,
            rtp_port=rtp_port,
        )

        component_options_rtsp.additional_properties = d
        return component_options_rtsp

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

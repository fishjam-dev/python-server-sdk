from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ComponentPropertiesRTSP")


@_attrs_define
class ComponentPropertiesRTSP:
    """Properties specific to the RTSP component"""

    keep_alive_interval: int
    """Interval (in ms) in which keep-alive RTSP messages will be sent to the remote stream source"""
    pierce_nat: bool
    """Whether to attempt to create client-side NAT binding by sending an empty datagram from client to source, after the completion of RTSP setup"""
    reconnect_delay: int
    """Delay (in ms) between successive reconnect attempts"""
    rtp_port: int
    """Local port RTP stream will be received at"""
    source_uri: str
    """URI of RTSP source stream"""
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)
    """@private"""

    def to_dict(self) -> Dict[str, Any]:
        """@private"""
        keep_alive_interval = self.keep_alive_interval
        pierce_nat = self.pierce_nat
        reconnect_delay = self.reconnect_delay
        rtp_port = self.rtp_port
        source_uri = self.source_uri

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "keepAliveInterval": keep_alive_interval,
                "pierceNat": pierce_nat,
                "reconnectDelay": reconnect_delay,
                "rtpPort": rtp_port,
                "sourceUri": source_uri,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        """@private"""
        d = src_dict.copy()
        keep_alive_interval = d.pop("keepAliveInterval")

        pierce_nat = d.pop("pierceNat")

        reconnect_delay = d.pop("reconnectDelay")

        rtp_port = d.pop("rtpPort")

        source_uri = d.pop("sourceUri")

        component_properties_rtsp = cls(
            keep_alive_interval=keep_alive_interval,
            pierce_nat=pierce_nat,
            reconnect_delay=reconnect_delay,
            rtp_port=rtp_port,
            source_uri=source_uri,
        )

        component_properties_rtsp.additional_properties = d
        return component_properties_rtsp

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

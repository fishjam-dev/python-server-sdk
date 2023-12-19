from typing import Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.component_properties_hls_subscribe_mode import (
    ComponentPropertiesHLSSubscribeMode,
)

T = TypeVar("T", bound="ComponentPropertiesHLS")


@_attrs_define
class ComponentPropertiesHLS:
    """Properties specific to the HLS component"""

    low_latency: bool
    """Whether the component uses LL-HLS"""
    persistent: bool
    """Whether the video is stored after end of stream"""
    playable: bool
    """Whether the generated HLS playlist is playable"""
    subscribe_mode: ComponentPropertiesHLSSubscribeMode
    """Whether the HLS component should subscribe to tracks automatically or manually"""
    target_window_duration: Optional[int]
    """Duration of stream available for viewer"""
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)
    """@private"""

    def to_dict(self) -> Dict[str, Any]:
        """@private"""
        low_latency = self.low_latency
        persistent = self.persistent
        playable = self.playable
        subscribe_mode = self.subscribe_mode.value

        target_window_duration = self.target_window_duration

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lowLatency": low_latency,
                "persistent": persistent,
                "playable": playable,
                "subscribeMode": subscribe_mode,
                "targetWindowDuration": target_window_duration,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        """@private"""
        d = src_dict.copy()
        low_latency = d.pop("lowLatency")

        persistent = d.pop("persistent")

        playable = d.pop("playable")

        subscribe_mode = ComponentPropertiesHLSSubscribeMode(d.pop("subscribeMode"))

        target_window_duration = d.pop("targetWindowDuration")

        component_properties_hls = cls(
            low_latency=low_latency,
            persistent=persistent,
            playable=playable,
            subscribe_mode=subscribe_mode,
            target_window_duration=target_window_duration,
        )

        component_properties_hls.additional_properties = d
        return component_properties_hls

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

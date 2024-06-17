from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.component_options_hls_subscribe_mode import (
    ComponentOptionsHLSSubscribeMode,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.component_options_hlss3_credentials import (
        ComponentOptionsHLSS3Credentials,
    )


T = TypeVar("T", bound="ComponentOptionsHLS")


@_attrs_define
class ComponentOptionsHLS:
    """Options specific to the HLS component"""

    low_latency: Union[Unset, bool] = False
    """Whether the component should use LL-HLS"""
    persistent: Union[Unset, bool] = False
    """Whether the video is stored after end of stream"""
    s3: Union[Unset, None, "ComponentOptionsHLSS3Credentials"] = UNSET
    """An AWS S3 credential that will be used to send HLS stream. The stream will only be uploaded if credentials are provided"""
    subscribe_mode: Union[
        Unset, ComponentOptionsHLSSubscribeMode
    ] = ComponentOptionsHLSSubscribeMode.AUTO
    """Whether the HLS component should subscribe to tracks automatically or manually."""
    target_window_duration: Union[Unset, None, int] = UNSET
    """Duration of stream available for viewer"""
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)
    """@private"""

    def to_dict(self) -> Dict[str, Any]:
        """@private"""
        low_latency = self.low_latency
        persistent = self.persistent
        s3: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.s3, Unset):
            s3 = self.s3.to_dict() if self.s3 else None

        subscribe_mode: Union[Unset, str] = UNSET
        if not isinstance(self.subscribe_mode, Unset):
            subscribe_mode = self.subscribe_mode.value

        target_window_duration = self.target_window_duration

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if low_latency is not UNSET:
            field_dict["lowLatency"] = low_latency
        if persistent is not UNSET:
            field_dict["persistent"] = persistent
        if s3 is not UNSET:
            field_dict["s3"] = s3
        if subscribe_mode is not UNSET:
            field_dict["subscribeMode"] = subscribe_mode
        if target_window_duration is not UNSET:
            field_dict["targetWindowDuration"] = target_window_duration

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        """@private"""
        from ..models.component_options_hlss3_credentials import (
            ComponentOptionsHLSS3Credentials,
        )

        d = src_dict.copy()
        low_latency = d.pop("lowLatency", UNSET)

        persistent = d.pop("persistent", UNSET)

        _s3 = d.pop("s3", UNSET)
        s3: Union[Unset, None, ComponentOptionsHLSS3Credentials]
        if _s3 is None:
            s3 = None
        elif isinstance(_s3, Unset):
            s3 = UNSET
        else:
            s3 = ComponentOptionsHLSS3Credentials.from_dict(_s3)

        _subscribe_mode = d.pop("subscribeMode", UNSET)
        subscribe_mode: Union[Unset, ComponentOptionsHLSSubscribeMode]
        if isinstance(_subscribe_mode, Unset):
            subscribe_mode = UNSET
        else:
            subscribe_mode = ComponentOptionsHLSSubscribeMode(_subscribe_mode)

        target_window_duration = d.pop("targetWindowDuration", UNSET)

        component_options_hls = cls(
            low_latency=low_latency,
            persistent=persistent,
            s3=s3,
            subscribe_mode=subscribe_mode,
            target_window_duration=target_window_duration,
        )

        component_options_hls.additional_properties = d
        return component_options_hls

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

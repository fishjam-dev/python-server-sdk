from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.component_properties_recording_subscribe_mode import (
    ComponentPropertiesRecordingSubscribeMode,
)

T = TypeVar("T", bound="ComponentPropertiesRecording")


@_attrs_define
class ComponentPropertiesRecording:
    """Properties specific to the Recording component"""

    path_prefix: str
    """Path prefix under which all recording are stored"""
    subscribe_mode: ComponentPropertiesRecordingSubscribeMode
    """Whether the Recording component should subscribe to tracks automatically or manually"""
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)
    """@private"""

    def to_dict(self) -> Dict[str, Any]:
        """@private"""
        path_prefix = self.path_prefix
        subscribe_mode = self.subscribe_mode.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pathPrefix": path_prefix,
                "subscribeMode": subscribe_mode,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        """@private"""
        d = src_dict.copy()
        path_prefix = d.pop("pathPrefix")

        subscribe_mode = ComponentPropertiesRecordingSubscribeMode(
            d.pop("subscribeMode")
        )

        component_properties_recording = cls(
            path_prefix=path_prefix,
            subscribe_mode=subscribe_mode,
        )

        component_properties_recording.additional_properties = d
        return component_properties_recording

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

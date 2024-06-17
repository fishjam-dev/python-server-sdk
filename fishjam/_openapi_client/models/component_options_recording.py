from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.component_options_recording_subscribe_mode import (
    ComponentOptionsRecordingSubscribeMode,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.component_options_recording_s3_credentials import (
        ComponentOptionsRecordingS3Credentials,
    )


T = TypeVar("T", bound="ComponentOptionsRecording")


@_attrs_define
class ComponentOptionsRecording:
    """Options specific to the Recording component"""

    credentials: Union[Unset, None, "ComponentOptionsRecordingS3Credentials"] = UNSET
    """An AWS S3 credential that will be used to send HLS stream. The stream will only be uploaded if credentials are provided"""
    path_prefix: Union[Unset, None, str] = UNSET
    """Path prefix under which all recording are stored"""
    subscribe_mode: Union[
        Unset, ComponentOptionsRecordingSubscribeMode
    ] = ComponentOptionsRecordingSubscribeMode.AUTO
    """Whether the Recording component should subscribe to tracks automatically or manually."""
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)
    """@private"""

    def to_dict(self) -> Dict[str, Any]:
        """@private"""
        credentials: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = self.credentials.to_dict() if self.credentials else None

        path_prefix = self.path_prefix
        subscribe_mode: Union[Unset, str] = UNSET
        if not isinstance(self.subscribe_mode, Unset):
            subscribe_mode = self.subscribe_mode.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if path_prefix is not UNSET:
            field_dict["pathPrefix"] = path_prefix
        if subscribe_mode is not UNSET:
            field_dict["subscribeMode"] = subscribe_mode

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        """@private"""
        from ..models.component_options_recording_s3_credentials import (
            ComponentOptionsRecordingS3Credentials,
        )

        d = src_dict.copy()
        _credentials = d.pop("credentials", UNSET)
        credentials: Union[Unset, None, ComponentOptionsRecordingS3Credentials]
        if _credentials is None:
            credentials = None
        elif isinstance(_credentials, Unset):
            credentials = UNSET
        else:
            credentials = ComponentOptionsRecordingS3Credentials.from_dict(_credentials)

        path_prefix = d.pop("pathPrefix", UNSET)

        _subscribe_mode = d.pop("subscribeMode", UNSET)
        subscribe_mode: Union[Unset, ComponentOptionsRecordingSubscribeMode]
        if isinstance(_subscribe_mode, Unset):
            subscribe_mode = UNSET
        else:
            subscribe_mode = ComponentOptionsRecordingSubscribeMode(_subscribe_mode)

        component_options_recording = cls(
            credentials=credentials,
            path_prefix=path_prefix,
            subscribe_mode=subscribe_mode,
        )

        component_options_recording.additional_properties = d
        return component_options_recording

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

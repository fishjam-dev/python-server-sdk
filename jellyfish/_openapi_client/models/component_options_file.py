from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ComponentOptionsFile")


@_attrs_define
class ComponentOptionsFile:
    """Options specific to the File component"""

    file_path: str
    """Path to track file. Must be either OPUS encapsulated in Ogg or raw h264"""
    framerate: Union[Unset, None, int] = UNSET
    """Framerate of video in a file. It is only valid for video track"""
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)
    """@private"""

    def to_dict(self) -> Dict[str, Any]:
        """@private"""
        file_path = self.file_path
        framerate = self.framerate

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filePath": file_path,
            }
        )
        if framerate is not UNSET:
            field_dict["framerate"] = framerate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        """@private"""
        d = src_dict.copy()
        file_path = d.pop("filePath")

        framerate = d.pop("framerate", UNSET)

        component_options_file = cls(
            file_path=file_path,
            framerate=framerate,
        )

        component_options_file.additional_properties = d
        return component_options_file

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

from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    Type,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.component_file import ComponentFile
    from ..models.component_hls import ComponentHLS
    from ..models.component_recording import ComponentRecording
    from ..models.component_rtsp import ComponentRTSP
    from ..models.component_sip import ComponentSIP


T = TypeVar("T", bound="ComponentDetailsResponse")


@_attrs_define
class ComponentDetailsResponse:
    """Response containing component details"""

    data: Union[
        "ComponentFile",
        "ComponentHLS",
        "ComponentRTSP",
        "ComponentRecording",
        "ComponentSIP",
    ]
    """Describes component"""
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)
    """@private"""

    def to_dict(self) -> Dict[str, Any]:
        """@private"""
        from ..models.component_file import ComponentFile
        from ..models.component_hls import ComponentHLS
        from ..models.component_rtsp import ComponentRTSP
        from ..models.component_sip import ComponentSIP

        data: Dict[str, Any]

        if isinstance(self.data, ComponentHLS):
            data = self.data.to_dict()

        elif isinstance(self.data, ComponentRTSP):
            data = self.data.to_dict()

        elif isinstance(self.data, ComponentFile):
            data = self.data.to_dict()

        elif isinstance(self.data, ComponentSIP):
            data = self.data.to_dict()

        else:
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        """@private"""
        from ..models.component_file import ComponentFile
        from ..models.component_hls import ComponentHLS
        from ..models.component_recording import ComponentRecording
        from ..models.component_rtsp import ComponentRTSP
        from ..models.component_sip import ComponentSIP

        d = src_dict.copy()

        def _parse_data(
            data: object,
        ) -> Union[
            "ComponentFile",
            "ComponentHLS",
            "ComponentRTSP",
            "ComponentRecording",
            "ComponentSIP",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_component_type_0 = ComponentHLS.from_dict(data)

                return componentsschemas_component_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_component_type_1 = ComponentRTSP.from_dict(data)

                return componentsschemas_component_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_component_type_2 = ComponentFile.from_dict(data)

                return componentsschemas_component_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_component_type_3 = ComponentSIP.from_dict(data)

                return componentsschemas_component_type_3
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_component_type_4 = ComponentRecording.from_dict(data)

            return componentsschemas_component_type_4

        data = _parse_data(d.pop("data"))

        component_details_response = cls(
            data=data,
        )

        component_details_response.additional_properties = d
        return component_details_response

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

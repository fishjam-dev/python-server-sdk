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

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.component_options_file import ComponentOptionsFile
    from ..models.component_options_hls import ComponentOptionsHLS
    from ..models.component_options_recording import ComponentOptionsRecording
    from ..models.component_options_rtsp import ComponentOptionsRTSP
    from ..models.component_options_sip import ComponentOptionsSIP


T = TypeVar("T", bound="AddComponentJsonBody")


@_attrs_define
class AddComponentJsonBody:
    """ """

    type: str
    """Component type"""
    options: Union[
        "ComponentOptionsFile",
        "ComponentOptionsHLS",
        "ComponentOptionsRTSP",
        "ComponentOptionsRecording",
        "ComponentOptionsSIP",
        Unset,
    ] = UNSET
    """Component-specific options"""
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)
    """@private"""

    def to_dict(self) -> Dict[str, Any]:
        """@private"""
        from ..models.component_options_file import ComponentOptionsFile
        from ..models.component_options_hls import ComponentOptionsHLS
        from ..models.component_options_rtsp import ComponentOptionsRTSP
        from ..models.component_options_sip import ComponentOptionsSIP

        type = self.type
        options: Union[Dict[str, Any], Unset]
        if isinstance(self.options, Unset):
            options = UNSET

        elif isinstance(self.options, ComponentOptionsHLS):
            options = self.options.to_dict()

        elif isinstance(self.options, ComponentOptionsRTSP):
            options = self.options.to_dict()

        elif isinstance(self.options, ComponentOptionsFile):
            options = self.options.to_dict()

        elif isinstance(self.options, ComponentOptionsSIP):
            options = self.options.to_dict()

        else:
            options = self.options.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        """@private"""
        from ..models.component_options_file import ComponentOptionsFile
        from ..models.component_options_hls import ComponentOptionsHLS
        from ..models.component_options_recording import ComponentOptionsRecording
        from ..models.component_options_rtsp import ComponentOptionsRTSP
        from ..models.component_options_sip import ComponentOptionsSIP

        d = src_dict.copy()
        type = d.pop("type")

        def _parse_options(
            data: object,
        ) -> Union[
            "ComponentOptionsFile",
            "ComponentOptionsHLS",
            "ComponentOptionsRTSP",
            "ComponentOptionsRecording",
            "ComponentOptionsSIP",
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_component_options_type_0 = (
                    ComponentOptionsHLS.from_dict(data)
                )

                return componentsschemas_component_options_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_component_options_type_1 = (
                    ComponentOptionsRTSP.from_dict(data)
                )

                return componentsschemas_component_options_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_component_options_type_2 = (
                    ComponentOptionsFile.from_dict(data)
                )

                return componentsschemas_component_options_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_component_options_type_3 = (
                    ComponentOptionsSIP.from_dict(data)
                )

                return componentsschemas_component_options_type_3
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_component_options_type_4 = (
                ComponentOptionsRecording.from_dict(data)
            )

            return componentsschemas_component_options_type_4

        options = _parse_options(d.pop("options", UNSET))

        add_component_json_body = cls(
            type=type,
            options=options,
        )

        add_component_json_body.additional_properties = d
        return add_component_json_body

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

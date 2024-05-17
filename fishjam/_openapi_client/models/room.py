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
    from ..models.peer import Peer
    from ..models.room_config import RoomConfig


T = TypeVar("T", bound="Room")


@_attrs_define
class Room:
    """Description of the room state"""

    components: List[
        Union[
            "ComponentFile",
            "ComponentHLS",
            "ComponentRTSP",
            "ComponentRecording",
            "ComponentSIP",
        ]
    ]
    """List of all components"""
    config: "RoomConfig"
    """Room configuration"""
    id: str
    """Room ID"""
    peers: List["Peer"]
    """List of all peers"""
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)
    """@private"""

    def to_dict(self) -> Dict[str, Any]:
        """@private"""
        from ..models.component_file import ComponentFile
        from ..models.component_hls import ComponentHLS
        from ..models.component_rtsp import ComponentRTSP
        from ..models.component_sip import ComponentSIP

        components = []
        for components_item_data in self.components:
            components_item: Dict[str, Any]

            if isinstance(components_item_data, ComponentHLS):
                components_item = components_item_data.to_dict()

            elif isinstance(components_item_data, ComponentRTSP):
                components_item = components_item_data.to_dict()

            elif isinstance(components_item_data, ComponentFile):
                components_item = components_item_data.to_dict()

            elif isinstance(components_item_data, ComponentSIP):
                components_item = components_item_data.to_dict()

            else:
                components_item = components_item_data.to_dict()

            components.append(components_item)

        config = self.config.to_dict()

        id = self.id
        peers = []
        for peers_item_data in self.peers:
            peers_item = peers_item_data.to_dict()

            peers.append(peers_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "components": components,
                "config": config,
                "id": id,
                "peers": peers,
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
        from ..models.peer import Peer
        from ..models.room_config import RoomConfig

        d = src_dict.copy()
        components = []
        _components = d.pop("components")
        for components_item_data in _components:

            def _parse_components_item(
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

            components_item = _parse_components_item(components_item_data)

            components.append(components_item)

        config = RoomConfig.from_dict(d.pop("config"))

        id = d.pop("id")

        peers = []
        _peers = d.pop("peers")
        for peers_item_data in _peers:
            peers_item = Peer.from_dict(peers_item_data)

            peers.append(peers_item)

        room = cls(
            components=components,
            config=config,
            id=id,
            peers=peers,
        )

        room.additional_properties = d
        return room

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

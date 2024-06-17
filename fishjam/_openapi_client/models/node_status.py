from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.node_status_status import NodeStatusStatus

T = TypeVar("T", bound="NodeStatus")


@_attrs_define
class NodeStatus:
    """Informs about the status of node"""

    git_commit: str
    """Commit hash of the build"""
    node_name: str
    """Name of the node"""
    status: NodeStatusStatus
    """Informs about the status of Fishjam or a specific service"""
    uptime: int
    """Uptime of Fishjam (in seconds)"""
    version: str
    """Version of Fishjam"""
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)
    """@private"""

    def to_dict(self) -> Dict[str, Any]:
        """@private"""
        git_commit = self.git_commit
        node_name = self.node_name
        status = self.status.value

        uptime = self.uptime
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "gitCommit": git_commit,
                "nodeName": node_name,
                "status": status,
                "uptime": uptime,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        """@private"""
        d = src_dict.copy()
        git_commit = d.pop("gitCommit")

        node_name = d.pop("nodeName")

        status = NodeStatusStatus(d.pop("status"))

        uptime = d.pop("uptime")

        version = d.pop("version")

        node_status = cls(
            git_commit=git_commit,
            node_name=node_name,
            status=status,
            uptime=uptime,
            version=version,
        )

        node_status.additional_properties = d
        return node_status

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

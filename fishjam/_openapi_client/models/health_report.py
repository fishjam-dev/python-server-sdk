from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.node_status import NodeStatus


T = TypeVar("T", bound="HealthReport")


@_attrs_define
class HealthReport:
    """Describes overall Fishjam health"""

    distribution_enabled: bool
    """Cluster distribution enabled/disabled"""
    local_status: "NodeStatus"
    """Informs about the status of node"""
    nodes_in_cluster: int
    """Number of nodes in cluster"""
    nodes_status: List["NodeStatus"]
    """Status of each node in cluster"""
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)
    """@private"""

    def to_dict(self) -> Dict[str, Any]:
        """@private"""
        distribution_enabled = self.distribution_enabled
        local_status = self.local_status.to_dict()

        nodes_in_cluster = self.nodes_in_cluster
        nodes_status = []
        for nodes_status_item_data in self.nodes_status:
            nodes_status_item = nodes_status_item_data.to_dict()

            nodes_status.append(nodes_status_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "distributionEnabled": distribution_enabled,
                "localStatus": local_status,
                "nodesInCluster": nodes_in_cluster,
                "nodesStatus": nodes_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        """@private"""
        from ..models.node_status import NodeStatus

        d = src_dict.copy()
        distribution_enabled = d.pop("distributionEnabled")

        local_status = NodeStatus.from_dict(d.pop("localStatus"))

        nodes_in_cluster = d.pop("nodesInCluster")

        nodes_status = []
        _nodes_status = d.pop("nodesStatus")
        for nodes_status_item_data in _nodes_status:
            nodes_status_item = NodeStatus.from_dict(nodes_status_item_data)

            nodes_status.append(nodes_status_item)

        health_report = cls(
            distribution_enabled=distribution_enabled,
            local_status=local_status,
            nodes_in_cluster=nodes_in_cluster,
            nodes_status=nodes_status,
        )

        health_report.additional_properties = d
        return health_report

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

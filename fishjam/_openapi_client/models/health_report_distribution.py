from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.health_report_status import HealthReportStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="HealthReportDistribution")


@_attrs_define
class HealthReportDistribution:
    """Informs about the status of Fishjam distribution"""

    node_status: HealthReportStatus
    """Informs about the status of Fishjam or a specific service"""
    nodes_in_cluster: int
    """Amount of nodes (including this Fishjam's node) in the distribution cluster"""
    enabled: Union[Unset, bool] = UNSET
    """Whether distribution is enabled on this Fishjam"""
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)
    """@private"""

    def to_dict(self) -> Dict[str, Any]:
        """@private"""
        node_status = self.node_status.value

        nodes_in_cluster = self.nodes_in_cluster
        enabled = self.enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nodeStatus": node_status,
                "nodesInCluster": nodes_in_cluster,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        """@private"""
        d = src_dict.copy()
        node_status = HealthReportStatus(d.pop("nodeStatus"))

        nodes_in_cluster = d.pop("nodesInCluster")

        enabled = d.pop("enabled", UNSET)

        health_report_distribution = cls(
            node_status=node_status,
            nodes_in_cluster=nodes_in_cluster,
            enabled=enabled,
        )

        health_report_distribution.additional_properties = d
        return health_report_distribution

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

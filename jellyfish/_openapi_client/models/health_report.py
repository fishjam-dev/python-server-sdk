from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.health_report_status import HealthReportStatus

if TYPE_CHECKING:
    from ..models.health_report_distribution import HealthReportDistribution


T = TypeVar("T", bound="HealthReport")


@_attrs_define
class HealthReport:
    """Describes overall Jellyfish health"""

    distribution: "HealthReportDistribution"
    """Informs about the status of Jellyfish distribution"""
    git_commit: str
    """Commit hash of the build"""
    status: HealthReportStatus
    """Informs about the status of Jellyfish or a specific service"""
    uptime: int
    """Uptime of Jellyfish (in seconds)"""
    version: str
    """Version of Jellyfish"""
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)
    """@private"""

    def to_dict(self) -> Dict[str, Any]:
        """@private"""
        distribution = self.distribution.to_dict()

        git_commit = self.git_commit
        status = self.status.value

        uptime = self.uptime
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "distribution": distribution,
                "gitCommit": git_commit,
                "status": status,
                "uptime": uptime,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        """@private"""
        from ..models.health_report_distribution import HealthReportDistribution

        d = src_dict.copy()
        distribution = HealthReportDistribution.from_dict(d.pop("distribution"))

        git_commit = d.pop("gitCommit")

        status = HealthReportStatus(d.pop("status"))

        uptime = d.pop("uptime")

        version = d.pop("version")

        health_report = cls(
            distribution=distribution,
            git_commit=git_commit,
            status=status,
            uptime=uptime,
            version=version,
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

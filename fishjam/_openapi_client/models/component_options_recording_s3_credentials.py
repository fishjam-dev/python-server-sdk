from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ComponentOptionsRecordingS3Credentials")


@_attrs_define
class ComponentOptionsRecordingS3Credentials:
    """An AWS S3 credential that will be used to send HLS stream. The stream will only be uploaded if credentials are
    provided

    """

    access_key_id: str
    """An AWS access key identifier, linked to your AWS account."""
    bucket: str
    """The name of the S3 bucket where your data will be stored."""
    region: str
    """The AWS region where your bucket is located."""
    secret_access_key: str
    """The secret key that is linked to the Access Key ID."""
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)
    """@private"""

    def to_dict(self) -> Dict[str, Any]:
        """@private"""
        access_key_id = self.access_key_id
        bucket = self.bucket
        region = self.region
        secret_access_key = self.secret_access_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accessKeyId": access_key_id,
                "bucket": bucket,
                "region": region,
                "secretAccessKey": secret_access_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        """@private"""
        d = src_dict.copy()
        access_key_id = d.pop("accessKeyId")

        bucket = d.pop("bucket")

        region = d.pop("region")

        secret_access_key = d.pop("secretAccessKey")

        component_options_recording_s3_credentials = cls(
            access_key_id=access_key_id,
            bucket=bucket,
            region=region,
            secret_access_key=secret_access_key,
        )

        component_options_recording_s3_credentials.additional_properties = d
        return component_options_recording_s3_credentials

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

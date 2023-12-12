from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.peer import Peer


T = TypeVar("T", bound="PeerDetailsResponseData")


@_attrs_define
class PeerDetailsResponseData:
    """
    Attributes:
        peer (Peer): Describes peer status
        token (str): Token for authorizing websocket connection Example: 5cdac726-57a3-4ecb-b1d5-72a3d62ec242.
    """

    peer: "Peer"
    token: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        peer = self.peer.to_dict()

        token = self.token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "peer": peer,
                "token": token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.peer import Peer

        d = src_dict.copy()
        peer = Peer.from_dict(d.pop("peer"))

        token = d.pop("token")

        peer_details_response_data = cls(
            peer=peer,
            token=token,
        )

        peer_details_response_data.additional_properties = d
        return peer_details_response_data

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

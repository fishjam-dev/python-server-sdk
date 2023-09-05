# Peer

Describes peer status

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Assigned peer id | 
**status** | [**PeerStatus**](PeerStatus.md) |  | 
**type** | **str** | Peer type | 

## Example

```python
from jellyfish_openapi_client.models.peer import Peer

# TODO update the JSON string below
json = "{}"
# create an instance of Peer from a JSON string
peer_instance = Peer.from_json(json)
# print the JSON string representation of the object
print Peer.to_json()

# convert the object into a dict
peer_dict = peer_instance.to_dict()
# create an instance of Peer from a dict
peer_form_dict = peer.from_dict(peer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



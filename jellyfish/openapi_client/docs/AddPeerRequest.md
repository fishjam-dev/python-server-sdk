# AddPeerRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | [**PeerOptions**](PeerOptions.md) |  | 
**type** | **str** | Peer type | 

## Example

```python
from jellyfish_openapi_client.models.add_peer_request import AddPeerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddPeerRequest from a JSON string
add_peer_request_instance = AddPeerRequest.from_json(json)
# print the JSON string representation of the object
print AddPeerRequest.to_json()

# convert the object into a dict
add_peer_request_dict = add_peer_request_instance.to_dict()
# create an instance of AddPeerRequest from a dict
add_peer_request_form_dict = add_peer_request.from_dict(add_peer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



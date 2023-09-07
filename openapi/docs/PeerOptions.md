# PeerOptions

Peer-specific options

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_simulcast** | **bool** | Enables the peer to use simulcast | [optional] [default to True]

## Example

```python
from openapi_client.models.peer_options import PeerOptions

# TODO update the JSON string below
json = "{}"
# create an instance of PeerOptions from a JSON string
peer_options_instance = PeerOptions.from_json(json)
# print the JSON string representation of the object
print PeerOptions.to_json()

# convert the object into a dict
peer_options_dict = peer_options_instance.to_dict()
# create an instance of PeerOptions from a dict
peer_options_form_dict = peer_options.from_dict(peer_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



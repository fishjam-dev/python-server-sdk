# PeerDetailsResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**peer** | [**Peer**](Peer.md) |  | 
**token** | **str** | Token for authorizing websocket connection | 

## Example

```python
from openapi_client.models.peer_details_response_data import PeerDetailsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PeerDetailsResponseData from a JSON string
peer_details_response_data_instance = PeerDetailsResponseData.from_json(json)
# print the JSON string representation of the object
print PeerDetailsResponseData.to_json()

# convert the object into a dict
peer_details_response_data_dict = peer_details_response_data_instance.to_dict()
# create an instance of PeerDetailsResponseData from a dict
peer_details_response_data_form_dict = peer_details_response_data.from_dict(peer_details_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



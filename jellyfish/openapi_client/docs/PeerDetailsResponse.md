# PeerDetailsResponse

Response containing peer details and their token

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PeerDetailsResponseData**](PeerDetailsResponseData.md) |  | 

## Example

```python
from jellyfish_openapi_client.models.peer_details_response import PeerDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PeerDetailsResponse from a JSON string
peer_details_response_instance = PeerDetailsResponse.from_json(json)
# print the JSON string representation of the object
print PeerDetailsResponse.to_json()

# convert the object into a dict
peer_details_response_dict = peer_details_response_instance.to_dict()
# create an instance of PeerDetailsResponse from a dict
peer_details_response_form_dict = peer_details_response.from_dict(peer_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



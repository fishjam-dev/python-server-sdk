# RoomsListingResponse

Response containing list of all rooms

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Room]**](Room.md) |  | 

## Example

```python
from jellyfish_openapi_client.models.rooms_listing_response import RoomsListingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RoomsListingResponse from a JSON string
rooms_listing_response_instance = RoomsListingResponse.from_json(json)
# print the JSON string representation of the object
print RoomsListingResponse.to_json()

# convert the object into a dict
rooms_listing_response_dict = rooms_listing_response_instance.to_dict()
# create an instance of RoomsListingResponse from a dict
rooms_listing_response_form_dict = rooms_listing_response.from_dict(rooms_listing_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



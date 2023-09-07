# RoomCreateDetailsResponse

Response containing room details

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**RoomCreateDetailsResponseData**](RoomCreateDetailsResponseData.md) |  | 

## Example

```python
from openapi_client.models.room_create_details_response import RoomCreateDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RoomCreateDetailsResponse from a JSON string
room_create_details_response_instance = RoomCreateDetailsResponse.from_json(json)
# print the JSON string representation of the object
print RoomCreateDetailsResponse.to_json()

# convert the object into a dict
room_create_details_response_dict = room_create_details_response_instance.to_dict()
# create an instance of RoomCreateDetailsResponse from a dict
room_create_details_response_form_dict = room_create_details_response.from_dict(room_create_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



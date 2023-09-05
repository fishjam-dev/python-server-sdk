# RoomDetailsResponse

Response containing room details

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Room**](Room.md) |  | 

## Example

```python
from jellyfish_openapi_client.models.room_details_response import RoomDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RoomDetailsResponse from a JSON string
room_details_response_instance = RoomDetailsResponse.from_json(json)
# print the JSON string representation of the object
print RoomDetailsResponse.to_json()

# convert the object into a dict
room_details_response_dict = room_details_response_instance.to_dict()
# create an instance of RoomDetailsResponse from a dict
room_details_response_form_dict = room_details_response.from_dict(room_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



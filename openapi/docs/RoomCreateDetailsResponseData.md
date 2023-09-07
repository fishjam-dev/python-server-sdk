# RoomCreateDetailsResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jellyfish_address** | **str** | Jellyfish instance address where the room was created. This might be different than the address of Jellyfish where the request was sent only when running a cluster of Jellyfishes. | 
**room** | [**Room**](Room.md) |  | 

## Example

```python
from openapi_client.models.room_create_details_response_data import RoomCreateDetailsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of RoomCreateDetailsResponseData from a JSON string
room_create_details_response_data_instance = RoomCreateDetailsResponseData.from_json(json)
# print the JSON string representation of the object
print RoomCreateDetailsResponseData.to_json()

# convert the object into a dict
room_create_details_response_data_dict = room_create_details_response_data_instance.to_dict()
# create an instance of RoomCreateDetailsResponseData from a dict
room_create_details_response_data_form_dict = room_create_details_response_data.from_dict(room_create_details_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



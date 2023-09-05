# RoomConfig

Room configuration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_peers** | **int** | Maximum amount of peers allowed into the room | [optional] 
**video_codec** | **str** | Enforces video codec for each peer in the room | [optional] 

## Example

```python
from jellyfish_openapi_client.models.room_config import RoomConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RoomConfig from a JSON string
room_config_instance = RoomConfig.from_json(json)
# print the JSON string representation of the object
print RoomConfig.to_json()

# convert the object into a dict
room_config_dict = room_config_instance.to_dict()
# create an instance of RoomConfig from a dict
room_config_form_dict = room_config.from_dict(room_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Room

Description of the room state

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**components** | [**List[Component]**](Component.md) |  | 
**config** | [**RoomConfig**](RoomConfig.md) |  | 
**id** | **str** | Room ID | 
**peers** | [**List[Peer]**](Peer.md) |  | 

## Example

```python
from openapi_client.models.room import Room

# TODO update the JSON string below
json = "{}"
# create an instance of Room from a JSON string
room_instance = Room.from_json(json)
# print the JSON string representation of the object
print Room.to_json()

# convert the object into a dict
room_dict = room_instance.to_dict()
# create an instance of Room from a dict
room_form_dict = room.from_dict(room_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



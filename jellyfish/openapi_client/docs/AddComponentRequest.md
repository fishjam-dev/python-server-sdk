# AddComponentRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | [**ComponentOptions**](ComponentOptions.md) |  | 
**type** | **str** | Component type | 

## Example

```python
from jellyfish_openapi_client.models.add_component_request import AddComponentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddComponentRequest from a JSON string
add_component_request_instance = AddComponentRequest.from_json(json)
# print the JSON string representation of the object
print AddComponentRequest.to_json()

# convert the object into a dict
add_component_request_dict = add_component_request_instance.to_dict()
# create an instance of AddComponentRequest from a dict
add_component_request_form_dict = add_component_request.from_dict(add_component_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



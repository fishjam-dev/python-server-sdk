# Component

Describes component

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Assigned component id | 
**metadata** | [**ComponentMetadata**](ComponentMetadata.md) |  | 
**type** | **str** | Component type | 

## Example

```python
from jellyfish_openapi_client.models.component import Component

# TODO update the JSON string below
json = "{}"
# create an instance of Component from a JSON string
component_instance = Component.from_json(json)
# print the JSON string representation of the object
print Component.to_json()

# convert the object into a dict
component_dict = component_instance.to_dict()
# create an instance of Component from a dict
component_form_dict = component.from_dict(component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



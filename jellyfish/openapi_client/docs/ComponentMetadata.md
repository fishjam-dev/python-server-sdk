# ComponentMetadata

Component-specific metadata

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**playable** | **bool** |  | [optional] 

## Example

```python
from jellyfish_openapi_client.models.component_metadata import ComponentMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ComponentMetadata from a JSON string
component_metadata_instance = ComponentMetadata.from_json(json)
# print the JSON string representation of the object
print ComponentMetadata.to_json()

# convert the object into a dict
component_metadata_dict = component_metadata_instance.to_dict()
# create an instance of ComponentMetadata from a dict
component_metadata_form_dict = component_metadata.from_dict(component_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



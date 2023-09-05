# ComponentOptions

Component-specific options

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keep_alive_interval** | **int** | Interval (in ms) in which keep-alive RTSP messages will be sent to the remote stream source | [optional] [default to 15000]
**pierce_nat** | **bool** | Whether to attempt to create client-side NAT binding by sending an empty datagram from client to source, after the completion of RTSP setup | [optional] [default to True]
**reconnect_delay** | **int** | Delay (in ms) between successive reconnect attempts | [optional] [default to 15000]
**rtp_port** | **int** | Local port RTP stream will be received at | [optional] [default to 20000]
**source_uri** | **str** | URI of RTSP source stream | 

## Example

```python
from jellyfish_openapi_client.models.component_options import ComponentOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ComponentOptions from a JSON string
component_options_instance = ComponentOptions.from_json(json)
# print the JSON string representation of the object
print ComponentOptions.to_json()

# convert the object into a dict
component_options_dict = component_options_instance.to_dict()
# create an instance of ComponentOptions from a dict
component_options_form_dict = component_options.from_dict(component_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



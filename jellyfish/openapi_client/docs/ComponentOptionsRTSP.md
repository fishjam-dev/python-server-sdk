# ComponentOptionsRTSP

Options specific to the RTSP component

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
from jellyfish_openapi_client.models.component_options_rtsp import ComponentOptionsRTSP

# TODO update the JSON string below
json = "{}"
# create an instance of ComponentOptionsRTSP from a JSON string
component_options_rtsp_instance = ComponentOptionsRTSP.from_json(json)
# print the JSON string representation of the object
print ComponentOptionsRTSP.to_json()

# convert the object into a dict
component_options_rtsp_dict = component_options_rtsp_instance.to_dict()
# create an instance of ComponentOptionsRTSP from a dict
component_options_rtsp_form_dict = component_options_rtsp.from_dict(component_options_rtsp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



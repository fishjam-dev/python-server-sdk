# PeerOptionsWebRTC

Options specific to the WebRTC peer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_simulcast** | **bool** | Enables the peer to use simulcast | [optional] [default to True]

## Example

```python
from openapi_client.models.peer_options_web_rtc import PeerOptionsWebRTC

# TODO update the JSON string below
json = "{}"
# create an instance of PeerOptionsWebRTC from a JSON string
peer_options_web_rtc_instance = PeerOptionsWebRTC.from_json(json)
# print the JSON string representation of the object
print PeerOptionsWebRTC.to_json()

# convert the object into a dict
peer_options_web_rtc_dict = peer_options_web_rtc_instance.to_dict()
# create an instance of PeerOptionsWebRTC from a dict
peer_options_web_rtc_form_dict = peer_options_web_rtc.from_dict(peer_options_web_rtc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



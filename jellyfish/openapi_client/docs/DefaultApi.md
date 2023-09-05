# jellyfish_openapi_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jellyfish_web_hls_controller_index**](DefaultApi.md#jellyfish_web_hls_controller_index) | **GET** /hls/{room_id}/{filename} | Send file


# **jellyfish_web_hls_controller_index**
> str jellyfish_web_hls_controller_index(room_id, filename, range=range, hls_msn=hls_msn, hls_part=hls_part, hls_skip=hls_skip)

Send file

### Example

* Bearer Authentication (authorization):
```python
import time
import os
import jellyfish_openapi_client
from jellyfish_openapi_client.models.hls_skip import HlsSkip
from jellyfish_openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = jellyfish_openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authorization
configuration = jellyfish_openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with jellyfish_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jellyfish_openapi_client.DefaultApi(api_client)
    room_id = 'room_id_example' # str | Room id
    filename = 'filename_example' # str | Name of the file
    range = 'range_example' # str | Byte range of partial segment (optional)
    hls_msn = 56 # int | Segment sequence number (optional)
    hls_part = 56 # int | Partial segment sequence number (optional)
    hls_skip = jellyfish_openapi_client.HlsSkip() # HlsSkip | Is delta manifest requested (optional)

    try:
        # Send file
        api_response = api_instance.jellyfish_web_hls_controller_index(room_id, filename, range=range, hls_msn=hls_msn, hls_part=hls_part, hls_skip=hls_skip)
        print("The response of DefaultApi->jellyfish_web_hls_controller_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->jellyfish_web_hls_controller_index: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_id** | **str**| Room id | 
 **filename** | **str**| Name of the file | 
 **range** | **str**| Byte range of partial segment | [optional] 
 **hls_msn** | **int**| Segment sequence number | [optional] 
 **hls_part** | **int**| Partial segment sequence number | [optional] 
 **hls_skip** | [**HlsSkip**](.md)| Is delta manifest requested | [optional] 

### Return type

**str**

### Authorization

[authorization](../README.md#authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File was found |  -  |
**404** | File not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


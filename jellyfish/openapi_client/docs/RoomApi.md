# jellyfish_openapi_client.RoomApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_component**](RoomApi.md#add_component) | **POST** /room/{room_id}/component | Creates the component and adds it to the room
[**add_peer**](RoomApi.md#add_peer) | **POST** /room/{room_id}/peer | Create peer
[**create_room**](RoomApi.md#create_room) | **POST** /room | Creates a room
[**delete_component**](RoomApi.md#delete_component) | **DELETE** /room/{room_id}/component/{id} | Delete the component from the room
[**delete_peer**](RoomApi.md#delete_peer) | **DELETE** /room/{room_id}/peer/{id} | Delete peer
[**delete_room**](RoomApi.md#delete_room) | **DELETE** /room/{room_id} | Delete the room
[**get_all_rooms**](RoomApi.md#get_all_rooms) | **GET** /room | Show information about all rooms
[**get_room**](RoomApi.md#get_room) | **GET** /room/{room_id} | Shows information about the room


# **add_component**
> ComponentDetailsResponse add_component(room_id, add_component_request=add_component_request)

Creates the component and adds it to the room

### Example

* Bearer Authentication (authorization):
```python
import time
import os
import jellyfish_openapi_client
from jellyfish_openapi_client.models.add_component_request import AddComponentRequest
from jellyfish_openapi_client.models.component_details_response import ComponentDetailsResponse
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
    api_instance = jellyfish_openapi_client.RoomApi(api_client)
    room_id = 'room_id_example' # str | Room ID
    add_component_request = jellyfish_openapi_client.AddComponentRequest() # AddComponentRequest | Component config (optional)

    try:
        # Creates the component and adds it to the room
        api_response = api_instance.add_component(room_id, add_component_request=add_component_request)
        print("The response of RoomApi->add_component:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomApi->add_component: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_id** | **str**| Room ID | 
 **add_component_request** | [**AddComponentRequest**](AddComponentRequest.md)| Component config | [optional] 

### Return type

[**ComponentDetailsResponse**](ComponentDetailsResponse.md)

### Authorization

[authorization](../README.md#authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully added component |  -  |
**400** | Invalid request |  -  |
**401** | Unauthorized |  -  |
**404** | Room doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_peer**
> PeerDetailsResponse add_peer(room_id, add_peer_request=add_peer_request)

Create peer

### Example

* Bearer Authentication (authorization):
```python
import time
import os
import jellyfish_openapi_client
from jellyfish_openapi_client.models.add_peer_request import AddPeerRequest
from jellyfish_openapi_client.models.peer_details_response import PeerDetailsResponse
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
    api_instance = jellyfish_openapi_client.RoomApi(api_client)
    room_id = 'room_id_example' # str | Room id
    add_peer_request = jellyfish_openapi_client.AddPeerRequest() # AddPeerRequest | Peer specification (optional)

    try:
        # Create peer
        api_response = api_instance.add_peer(room_id, add_peer_request=add_peer_request)
        print("The response of RoomApi->add_peer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomApi->add_peer: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_id** | **str**| Room id | 
 **add_peer_request** | [**AddPeerRequest**](AddPeerRequest.md)| Peer specification | [optional] 

### Return type

[**PeerDetailsResponse**](PeerDetailsResponse.md)

### Authorization

[authorization](../README.md#authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Peer successfully created |  -  |
**400** | Invalid request body structure |  -  |
**401** | Unauthorized |  -  |
**404** | Room doesn&#39;t exist |  -  |
**503** | Peer limit has been reached |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_room**
> RoomCreateDetailsResponse create_room(room_config=room_config)

Creates a room

### Example

* Bearer Authentication (authorization):
```python
import time
import os
import jellyfish_openapi_client
from jellyfish_openapi_client.models.room_config import RoomConfig
from jellyfish_openapi_client.models.room_create_details_response import RoomCreateDetailsResponse
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
    api_instance = jellyfish_openapi_client.RoomApi(api_client)
    room_config = jellyfish_openapi_client.RoomConfig() # RoomConfig | Room configuration (optional)

    try:
        # Creates a room
        api_response = api_instance.create_room(room_config=room_config)
        print("The response of RoomApi->create_room:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomApi->create_room: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_config** | [**RoomConfig**](RoomConfig.md)| Room configuration | [optional] 

### Return type

[**RoomCreateDetailsResponse**](RoomCreateDetailsResponse.md)

### Authorization

[authorization](../README.md#authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Room successfully created |  -  |
**400** | Invalid request structure |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_component**
> delete_component(room_id, id)

Delete the component from the room

### Example

* Bearer Authentication (authorization):
```python
import time
import os
import jellyfish_openapi_client
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
    api_instance = jellyfish_openapi_client.RoomApi(api_client)
    room_id = 'room_id_example' # str | Room ID
    id = 'id_example' # str | Component ID

    try:
        # Delete the component from the room
        api_instance.delete_component(room_id, id)
    except Exception as e:
        print("Exception when calling RoomApi->delete_component: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_id** | **str**| Room ID | 
 **id** | **str**| Component ID | 

### Return type

void (empty response body)

### Authorization

[authorization](../README.md#authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successfully deleted |  -  |
**401** | Unauthorized |  -  |
**404** | Either component or the room doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_peer**
> delete_peer(room_id, id)

Delete peer

### Example

* Bearer Authentication (authorization):
```python
import time
import os
import jellyfish_openapi_client
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
    api_instance = jellyfish_openapi_client.RoomApi(api_client)
    room_id = 'room_id_example' # str | Room ID
    id = 'id_example' # str | Peer id

    try:
        # Delete peer
        api_instance.delete_peer(room_id, id)
    except Exception as e:
        print("Exception when calling RoomApi->delete_peer: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_id** | **str**| Room ID | 
 **id** | **str**| Peer id | 

### Return type

void (empty response body)

### Authorization

[authorization](../README.md#authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Peer successfully deleted |  -  |
**401** | Unauthorized |  -  |
**404** | Room ID or Peer ID references a resource that doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_room**
> delete_room(room_id)

Delete the room

### Example

* Bearer Authentication (authorization):
```python
import time
import os
import jellyfish_openapi_client
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
    api_instance = jellyfish_openapi_client.RoomApi(api_client)
    room_id = 'room_id_example' # str | Room id

    try:
        # Delete the room
        api_instance.delete_room(room_id)
    except Exception as e:
        print("Exception when calling RoomApi->delete_room: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_id** | **str**| Room id | 

### Return type

void (empty response body)

### Authorization

[authorization](../README.md#authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successfully deleted room |  -  |
**401** | Unauthorized |  -  |
**404** | Room doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_rooms**
> RoomsListingResponse get_all_rooms()

Show information about all rooms

### Example

* Bearer Authentication (authorization):
```python
import time
import os
import jellyfish_openapi_client
from jellyfish_openapi_client.models.rooms_listing_response import RoomsListingResponse
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
    api_instance = jellyfish_openapi_client.RoomApi(api_client)

    try:
        # Show information about all rooms
        api_response = api_instance.get_all_rooms()
        print("The response of RoomApi->get_all_rooms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomApi->get_all_rooms: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**RoomsListingResponse**](RoomsListingResponse.md)

### Authorization

[authorization](../README.md#authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_room**
> RoomDetailsResponse get_room(room_id)

Shows information about the room

### Example

* Bearer Authentication (authorization):
```python
import time
import os
import jellyfish_openapi_client
from jellyfish_openapi_client.models.room_details_response import RoomDetailsResponse
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
    api_instance = jellyfish_openapi_client.RoomApi(api_client)
    room_id = 'room_id_example' # str | Room ID

    try:
        # Shows information about the room
        api_response = api_instance.get_room(room_id)
        print("The response of RoomApi->get_room:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoomApi->get_room: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_id** | **str**| Room ID | 

### Return type

[**RoomDetailsResponse**](RoomDetailsResponse.md)

### Authorization

[authorization](../README.md#authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**404** | Room doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


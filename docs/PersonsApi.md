# simployer_client.PersonsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_persons_children_get**](PersonsApi.md#v1_persons_children_get) | **GET** /v1/persons/children | Retrieves children.
[**v1_persons_children_id_get**](PersonsApi.md#v1_persons_children_id_get) | **GET** /v1/persons/children/{id} | Retrieves child.
[**v1_persons_extended_properties_get**](PersonsApi.md#v1_persons_extended_properties_get) | **GET** /v1/persons/extendedProperties | Retrieves extended properties.
[**v1_persons_extended_properties_id_get**](PersonsApi.md#v1_persons_extended_properties_id_get) | **GET** /v1/persons/extendedProperties/{id} | Retrieves extended property with given value identifier.
[**v1_persons_extended_properties_type_id_get**](PersonsApi.md#v1_persons_extended_properties_type_id_get) | **GET** /v1/persons/extendedProperties/type/{id} | Retrieves extended properties with given type identifier.
[**v1_persons_get**](PersonsApi.md#v1_persons_get) | **GET** /v1/persons | Retrieves a paginated list of people.
[**v1_persons_id_children_get**](PersonsApi.md#v1_persons_id_children_get) | **GET** /v1/persons/{id}/children | Retrieves children for person.
[**v1_persons_id_extended_properties_get**](PersonsApi.md#v1_persons_id_extended_properties_get) | **GET** /v1/persons/{id}/extendedProperties | Retrieves extended properties for person.
[**v1_persons_id_get**](PersonsApi.md#v1_persons_id_get) | **GET** /v1/persons/{id} | Retrieves person with given identifier.
[**v1_persons_id_identity_identifiers_get**](PersonsApi.md#v1_persons_id_identity_identifiers_get) | **GET** /v1/persons/{id}/identityIdentifiers | Retrieves identity identifiers for given person.
[**v1_persons_id_next_of_kin_get**](PersonsApi.md#v1_persons_id_next_of_kin_get) | **GET** /v1/persons/{id}/nextOfKin | Retrieves next of kin for person.
[**v1_persons_identity_identifiers_get**](PersonsApi.md#v1_persons_identity_identifiers_get) | **GET** /v1/persons/identityIdentifiers | Retrieves identity identifiers.
[**v1_persons_identity_identifiers_id_get**](PersonsApi.md#v1_persons_identity_identifiers_id_get) | **GET** /v1/persons/identityIdentifiers/{id} | Retrieves identity identifiers with given identifier.
[**v1_persons_manager_structure_get**](PersonsApi.md#v1_persons_manager_structure_get) | **GET** /v1/persons/managerStructure | Retrieves the manager structure.
[**v1_persons_next_of_kin_get**](PersonsApi.md#v1_persons_next_of_kin_get) | **GET** /v1/persons/nextOfKin | Retrieves next of kin.
[**v1_persons_next_of_kin_id_get**](PersonsApi.md#v1_persons_next_of_kin_id_get) | **GET** /v1/persons/nextOfKin/{id} | Retrieves next of kin.


# **v1_persons_children_get**
> List[Child] v1_persons_children_get(page=page, page_size=page_size)

Retrieves children.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.child import Child
from simployer_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = simployer_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with simployer_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = simployer_client.PersonsApi(api_client)
    page = 1 # int | Page number (default is 1). (optional) (default to 1)
    page_size = 100 # int | Number of items per page (default is 100). (optional) (default to 100)

    try:
        # Retrieves children.
        api_response = api_instance.v1_persons_children_get(page=page, page_size=page_size)
        print("The response of PersonsApi->v1_persons_children_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->v1_persons_children_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number (default is 1). | [optional] [default to 1]
 **page_size** | **int**| Number of items per page (default is 100). | [optional] [default to 100]

### Return type

[**List[Child]**](Child.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_persons_children_id_get**
> Child v1_persons_children_id_get(id)

Retrieves child.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.child import Child
from simployer_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = simployer_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with simployer_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = simployer_client.PersonsApi(api_client)
    id = 'id_example' # str | Identifier of child.

    try:
        # Retrieves child.
        api_response = api_instance.v1_persons_children_id_get(id)
        print("The response of PersonsApi->v1_persons_children_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->v1_persons_children_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of child. | 

### Return type

[**Child**](Child.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_persons_extended_properties_get**
> ExtendedPropertyPagination v1_persons_extended_properties_get(page=page, page_size=page_size)

Retrieves extended properties.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.extended_property_pagination import ExtendedPropertyPagination
from simployer_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = simployer_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with simployer_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = simployer_client.PersonsApi(api_client)
    page = 1 # int | Page number (default is 1). (optional) (default to 1)
    page_size = 100 # int | Number of items per page (default is 100). (optional) (default to 100)

    try:
        # Retrieves extended properties.
        api_response = api_instance.v1_persons_extended_properties_get(page=page, page_size=page_size)
        print("The response of PersonsApi->v1_persons_extended_properties_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->v1_persons_extended_properties_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number (default is 1). | [optional] [default to 1]
 **page_size** | **int**| Number of items per page (default is 100). | [optional] [default to 100]

### Return type

[**ExtendedPropertyPagination**](ExtendedPropertyPagination.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_persons_extended_properties_id_get**
> ExtendedProperty v1_persons_extended_properties_id_get(id)

Retrieves extended property with given value identifier.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.extended_property import ExtendedProperty
from simployer_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = simployer_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with simployer_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = simployer_client.PersonsApi(api_client)
    id = 'id_example' # str | Identifier of value.

    try:
        # Retrieves extended property with given value identifier.
        api_response = api_instance.v1_persons_extended_properties_id_get(id)
        print("The response of PersonsApi->v1_persons_extended_properties_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->v1_persons_extended_properties_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of value. | 

### Return type

[**ExtendedProperty**](ExtendedProperty.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_persons_extended_properties_type_id_get**
> List[ExtendedProperty] v1_persons_extended_properties_type_id_get(id)

Retrieves extended properties with given type identifier.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.extended_property import ExtendedProperty
from simployer_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = simployer_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with simployer_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = simployer_client.PersonsApi(api_client)
    id = 'id_example' # str | Identifier of type.

    try:
        # Retrieves extended properties with given type identifier.
        api_response = api_instance.v1_persons_extended_properties_type_id_get(id)
        print("The response of PersonsApi->v1_persons_extended_properties_type_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->v1_persons_extended_properties_type_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of type. | 

### Return type

[**List[ExtendedProperty]**](ExtendedProperty.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_persons_get**
> List[Person] v1_persons_get(page=page, page_size=page_size)

Retrieves a paginated list of people.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.person import Person
from simployer_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = simployer_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with simployer_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = simployer_client.PersonsApi(api_client)
    page = 1 # int | Page number (default is 1). (optional) (default to 1)
    page_size = 100 # int | Number of items per page (default is 100). (optional) (default to 100)

    try:
        # Retrieves a paginated list of people.
        api_response = api_instance.v1_persons_get(page=page, page_size=page_size)
        print("The response of PersonsApi->v1_persons_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->v1_persons_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number (default is 1). | [optional] [default to 1]
 **page_size** | **int**| Number of items per page (default is 100). | [optional] [default to 100]

### Return type

[**List[Person]**](Person.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_persons_id_children_get**
> List[Child] v1_persons_id_children_get(id)

Retrieves children for person.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.child import Child
from simployer_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = simployer_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with simployer_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = simployer_client.PersonsApi(api_client)
    id = 'id_example' # str | Identifier of person.

    try:
        # Retrieves children for person.
        api_response = api_instance.v1_persons_id_children_get(id)
        print("The response of PersonsApi->v1_persons_id_children_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->v1_persons_id_children_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of person. | 

### Return type

[**List[Child]**](Child.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_persons_id_extended_properties_get**
> List[ExtendedProperty] v1_persons_id_extended_properties_get(id)

Retrieves extended properties for person.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.extended_property import ExtendedProperty
from simployer_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = simployer_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with simployer_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = simployer_client.PersonsApi(api_client)
    id = 'id_example' # str | Identifier of person.

    try:
        # Retrieves extended properties for person.
        api_response = api_instance.v1_persons_id_extended_properties_get(id)
        print("The response of PersonsApi->v1_persons_id_extended_properties_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->v1_persons_id_extended_properties_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of person. | 

### Return type

[**List[ExtendedProperty]**](ExtendedProperty.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_persons_id_get**
> Person v1_persons_id_get(id)

Retrieves person with given identifier.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.person import Person
from simployer_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = simployer_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with simployer_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = simployer_client.PersonsApi(api_client)
    id = 'id_example' # str | Identifier of person.

    try:
        # Retrieves person with given identifier.
        api_response = api_instance.v1_persons_id_get(id)
        print("The response of PersonsApi->v1_persons_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->v1_persons_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of person. | 

### Return type

[**Person**](Person.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | No Content |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_persons_id_identity_identifiers_get**
> List[IdentityIdentifier] v1_persons_id_identity_identifiers_get(id)

Retrieves identity identifiers for given person.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.identity_identifier import IdentityIdentifier
from simployer_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = simployer_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with simployer_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = simployer_client.PersonsApi(api_client)
    id = 'id_example' # str | Identifier of person.

    try:
        # Retrieves identity identifiers for given person.
        api_response = api_instance.v1_persons_id_identity_identifiers_get(id)
        print("The response of PersonsApi->v1_persons_id_identity_identifiers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->v1_persons_id_identity_identifiers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of person. | 

### Return type

[**List[IdentityIdentifier]**](IdentityIdentifier.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_persons_id_next_of_kin_get**
> List[NextOfKin] v1_persons_id_next_of_kin_get(id)

Retrieves next of kin for person.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.next_of_kin import NextOfKin
from simployer_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = simployer_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with simployer_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = simployer_client.PersonsApi(api_client)
    id = 'id_example' # str | Identifier of person.

    try:
        # Retrieves next of kin for person.
        api_response = api_instance.v1_persons_id_next_of_kin_get(id)
        print("The response of PersonsApi->v1_persons_id_next_of_kin_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->v1_persons_id_next_of_kin_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of person. | 

### Return type

[**List[NextOfKin]**](NextOfKin.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_persons_identity_identifiers_get**
> List[IdentityIdentifier] v1_persons_identity_identifiers_get(page=page, page_size=page_size)

Retrieves identity identifiers.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.identity_identifier import IdentityIdentifier
from simployer_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = simployer_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with simployer_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = simployer_client.PersonsApi(api_client)
    page = 1 # int | Page number (default is 1). (optional) (default to 1)
    page_size = 100 # int | Number of items per page (default is 100). (optional) (default to 100)

    try:
        # Retrieves identity identifiers.
        api_response = api_instance.v1_persons_identity_identifiers_get(page=page, page_size=page_size)
        print("The response of PersonsApi->v1_persons_identity_identifiers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->v1_persons_identity_identifiers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number (default is 1). | [optional] [default to 1]
 **page_size** | **int**| Number of items per page (default is 100). | [optional] [default to 100]

### Return type

[**List[IdentityIdentifier]**](IdentityIdentifier.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_persons_identity_identifiers_id_get**
> List[IdentityIdentifier] v1_persons_identity_identifiers_id_get(id)

Retrieves identity identifiers with given identifier.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.identity_identifier import IdentityIdentifier
from simployer_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = simployer_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with simployer_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = simployer_client.PersonsApi(api_client)
    id = 'id_example' # str | Identifier of identity identifier.

    try:
        # Retrieves identity identifiers with given identifier.
        api_response = api_instance.v1_persons_identity_identifiers_id_get(id)
        print("The response of PersonsApi->v1_persons_identity_identifiers_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->v1_persons_identity_identifiers_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of identity identifier. | 

### Return type

[**List[IdentityIdentifier]**](IdentityIdentifier.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_persons_manager_structure_get**
> List[PersonManagerRelationship] v1_persons_manager_structure_get(page=page, page_size=page_size)

Retrieves the manager structure.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.person_manager_relationship import PersonManagerRelationship
from simployer_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = simployer_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with simployer_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = simployer_client.PersonsApi(api_client)
    page = 1 # int | Page number (default is 1). (optional) (default to 1)
    page_size = 100 # int | Number of items per page (default is 100). (optional) (default to 100)

    try:
        # Retrieves the manager structure.
        api_response = api_instance.v1_persons_manager_structure_get(page=page, page_size=page_size)
        print("The response of PersonsApi->v1_persons_manager_structure_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->v1_persons_manager_structure_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number (default is 1). | [optional] [default to 1]
 **page_size** | **int**| Number of items per page (default is 100). | [optional] [default to 100]

### Return type

[**List[PersonManagerRelationship]**](PersonManagerRelationship.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_persons_next_of_kin_get**
> List[NextOfKin] v1_persons_next_of_kin_get(page=page, page_size=page_size)

Retrieves next of kin.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.next_of_kin import NextOfKin
from simployer_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = simployer_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with simployer_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = simployer_client.PersonsApi(api_client)
    page = 1 # int | Page number (default is 1). (optional) (default to 1)
    page_size = 100 # int | Number of items per page (default is 100). (optional) (default to 100)

    try:
        # Retrieves next of kin.
        api_response = api_instance.v1_persons_next_of_kin_get(page=page, page_size=page_size)
        print("The response of PersonsApi->v1_persons_next_of_kin_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->v1_persons_next_of_kin_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number (default is 1). | [optional] [default to 1]
 **page_size** | **int**| Number of items per page (default is 100). | [optional] [default to 100]

### Return type

[**List[NextOfKin]**](NextOfKin.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_persons_next_of_kin_id_get**
> NextOfKin v1_persons_next_of_kin_id_get(id)

Retrieves next of kin.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.next_of_kin import NextOfKin
from simployer_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = simployer_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with simployer_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = simployer_client.PersonsApi(api_client)
    id = 'id_example' # str | Identifier of next of kin.

    try:
        # Retrieves next of kin.
        api_response = api_instance.v1_persons_next_of_kin_id_get(id)
        print("The response of PersonsApi->v1_persons_next_of_kin_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonsApi->v1_persons_next_of_kin_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of next of kin. | 

### Return type

[**NextOfKin**](NextOfKin.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# simployer_client.ContactsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_contacts_addresses_get**](ContactsApi.md#v1_contacts_addresses_get) | **GET** /v1/contacts/addresses | Retrieves addresses with pagination.
[**v1_contacts_addresses_id_get**](ContactsApi.md#v1_contacts_addresses_id_get) | **GET** /v1/contacts/addresses/{id} | Retrieves address with given identifier.
[**v1_contacts_addresses_unit_id_get**](ContactsApi.md#v1_contacts_addresses_unit_id_get) | **GET** /v1/contacts/addresses/unit/{id} | Retrieves addresses for unit.
[**v1_contacts_electronic_addresses_get**](ContactsApi.md#v1_contacts_electronic_addresses_get) | **GET** /v1/contacts/electronicAddresses | Retrieves electronic addresses with pagination.
[**v1_contacts_electronic_addresses_id_get**](ContactsApi.md#v1_contacts_electronic_addresses_id_get) | **GET** /v1/contacts/electronicAddresses/{id} | Retrieves electronic address with given identifier.
[**v1_contacts_electronic_addresses_unit_id_get**](ContactsApi.md#v1_contacts_electronic_addresses_unit_id_get) | **GET** /v1/contacts/electronicAddresses/unit/{id} | Retrieves electronic addresses for unit.
[**v1_contacts_phone_numbers_get**](ContactsApi.md#v1_contacts_phone_numbers_get) | **GET** /v1/contacts/phoneNumbers | Retrieves phone numbers with pagination.
[**v1_contacts_phone_numbers_id_get**](ContactsApi.md#v1_contacts_phone_numbers_id_get) | **GET** /v1/contacts/phoneNumbers/{id} | Retrieves phone number with given identifier.
[**v1_contacts_phone_numbers_unit_id_get**](ContactsApi.md#v1_contacts_phone_numbers_unit_id_get) | **GET** /v1/contacts/phoneNumbers/unit/{id} | Retrieves phone numbers for unit.


# **v1_contacts_addresses_get**
> List[Address] v1_contacts_addresses_get(unit_type=unit_type, page=page, page_size=page_size)

Retrieves addresses with pagination.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.address import Address
from simployer_client.models.unit_type import UnitType
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
    api_instance = simployer_client.ContactsApi(api_client)
    unit_type = simployer_client.UnitType() # UnitType | Unit type (default is NotSpecified). (optional)
    page = 1 # int | Page number (default is 1). (optional) (default to 1)
    page_size = 100 # int | Number of items per page (default is 100). (optional) (default to 100)

    try:
        # Retrieves addresses with pagination.
        api_response = api_instance.v1_contacts_addresses_get(unit_type=unit_type, page=page, page_size=page_size)
        print("The response of ContactsApi->v1_contacts_addresses_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->v1_contacts_addresses_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unit_type** | [**UnitType**](.md)| Unit type (default is NotSpecified). | [optional] 
 **page** | **int**| Page number (default is 1). | [optional] [default to 1]
 **page_size** | **int**| Number of items per page (default is 100). | [optional] [default to 100]

### Return type

[**List[Address]**](Address.md)

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

# **v1_contacts_addresses_id_get**
> Address v1_contacts_addresses_id_get(id)

Retrieves address with given identifier.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.address import Address
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
    api_instance = simployer_client.ContactsApi(api_client)
    id = 'id_example' # str | Identifier of the address.

    try:
        # Retrieves address with given identifier.
        api_response = api_instance.v1_contacts_addresses_id_get(id)
        print("The response of ContactsApi->v1_contacts_addresses_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->v1_contacts_addresses_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the address. | 

### Return type

[**Address**](Address.md)

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

# **v1_contacts_addresses_unit_id_get**
> List[Address] v1_contacts_addresses_unit_id_get(id)

Retrieves addresses for unit.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.address import Address
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
    api_instance = simployer_client.ContactsApi(api_client)
    id = 'id_example' # str | Identifier of unit that is owner of addresses.

    try:
        # Retrieves addresses for unit.
        api_response = api_instance.v1_contacts_addresses_unit_id_get(id)
        print("The response of ContactsApi->v1_contacts_addresses_unit_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->v1_contacts_addresses_unit_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of unit that is owner of addresses. | 

### Return type

[**List[Address]**](Address.md)

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

# **v1_contacts_electronic_addresses_get**
> List[ElectronicAddress] v1_contacts_electronic_addresses_get(unit_type=unit_type, page=page, page_size=page_size)

Retrieves electronic addresses with pagination.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.electronic_address import ElectronicAddress
from simployer_client.models.unit_type import UnitType
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
    api_instance = simployer_client.ContactsApi(api_client)
    unit_type = simployer_client.UnitType() # UnitType | Unit type (default is NotSpecified). (optional)
    page = 1 # int | Page number (default is 1). (optional) (default to 1)
    page_size = 100 # int | Number of items per page (default is 100). (optional) (default to 100)

    try:
        # Retrieves electronic addresses with pagination.
        api_response = api_instance.v1_contacts_electronic_addresses_get(unit_type=unit_type, page=page, page_size=page_size)
        print("The response of ContactsApi->v1_contacts_electronic_addresses_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->v1_contacts_electronic_addresses_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unit_type** | [**UnitType**](.md)| Unit type (default is NotSpecified). | [optional] 
 **page** | **int**| Page number (default is 1). | [optional] [default to 1]
 **page_size** | **int**| Number of items per page (default is 100). | [optional] [default to 100]

### Return type

[**List[ElectronicAddress]**](ElectronicAddress.md)

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

# **v1_contacts_electronic_addresses_id_get**
> ElectronicAddress v1_contacts_electronic_addresses_id_get(id)

Retrieves electronic address with given identifier.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.electronic_address import ElectronicAddress
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
    api_instance = simployer_client.ContactsApi(api_client)
    id = 'id_example' # str | Identifier of the electronic address.

    try:
        # Retrieves electronic address with given identifier.
        api_response = api_instance.v1_contacts_electronic_addresses_id_get(id)
        print("The response of ContactsApi->v1_contacts_electronic_addresses_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->v1_contacts_electronic_addresses_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the electronic address. | 

### Return type

[**ElectronicAddress**](ElectronicAddress.md)

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

# **v1_contacts_electronic_addresses_unit_id_get**
> List[ElectronicAddress] v1_contacts_electronic_addresses_unit_id_get(id)

Retrieves electronic addresses for unit.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.electronic_address import ElectronicAddress
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
    api_instance = simployer_client.ContactsApi(api_client)
    id = 'id_example' # str | Identifier of unit that is owner of electronic addresses.

    try:
        # Retrieves electronic addresses for unit.
        api_response = api_instance.v1_contacts_electronic_addresses_unit_id_get(id)
        print("The response of ContactsApi->v1_contacts_electronic_addresses_unit_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->v1_contacts_electronic_addresses_unit_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of unit that is owner of electronic addresses. | 

### Return type

[**List[ElectronicAddress]**](ElectronicAddress.md)

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

# **v1_contacts_phone_numbers_get**
> List[Phone] v1_contacts_phone_numbers_get(unit_type=unit_type, page=page, page_size=page_size)

Retrieves phone numbers with pagination.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.phone import Phone
from simployer_client.models.unit_type import UnitType
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
    api_instance = simployer_client.ContactsApi(api_client)
    unit_type = simployer_client.UnitType() # UnitType | Unit type (default is NotSpecified). (optional)
    page = 1 # int | Page number (default is 1). (optional) (default to 1)
    page_size = 100 # int | Number of items per page (default is 100). (optional) (default to 100)

    try:
        # Retrieves phone numbers with pagination.
        api_response = api_instance.v1_contacts_phone_numbers_get(unit_type=unit_type, page=page, page_size=page_size)
        print("The response of ContactsApi->v1_contacts_phone_numbers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->v1_contacts_phone_numbers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unit_type** | [**UnitType**](.md)| Unit type (default is NotSpecified). | [optional] 
 **page** | **int**| Page number (default is 1). | [optional] [default to 1]
 **page_size** | **int**| Number of items per page (default is 100). | [optional] [default to 100]

### Return type

[**List[Phone]**](Phone.md)

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

# **v1_contacts_phone_numbers_id_get**
> Phone v1_contacts_phone_numbers_id_get(id)

Retrieves phone number with given identifier.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.phone import Phone
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
    api_instance = simployer_client.ContactsApi(api_client)
    id = 'id_example' # str | Identifier of the phone number.

    try:
        # Retrieves phone number with given identifier.
        api_response = api_instance.v1_contacts_phone_numbers_id_get(id)
        print("The response of ContactsApi->v1_contacts_phone_numbers_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->v1_contacts_phone_numbers_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the phone number. | 

### Return type

[**Phone**](Phone.md)

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

# **v1_contacts_phone_numbers_unit_id_get**
> List[Phone] v1_contacts_phone_numbers_unit_id_get(id)

Retrieves phone numbers for unit.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.phone import Phone
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
    api_instance = simployer_client.ContactsApi(api_client)
    id = 'id_example' # str | Identifier of unit that is owner of phone numbers.

    try:
        # Retrieves phone numbers for unit.
        api_response = api_instance.v1_contacts_phone_numbers_unit_id_get(id)
        print("The response of ContactsApi->v1_contacts_phone_numbers_unit_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->v1_contacts_phone_numbers_unit_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of unit that is owner of phone numbers. | 

### Return type

[**List[Phone]**](Phone.md)

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


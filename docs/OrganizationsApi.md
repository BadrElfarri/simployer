# simployer_client.OrganizationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_organizations_get**](OrganizationsApi.md#v1_organizations_get) | **GET** /v1/organizations | Retrieves organizations with pagination.
[**v1_organizations_groups_affiliated_people_get**](OrganizationsApi.md#v1_organizations_groups_affiliated_people_get) | **GET** /v1/organizations/groups/affiliatedPeople | Retrieves group-people relations with pagination.
[**v1_organizations_groups_categories_get**](OrganizationsApi.md#v1_organizations_groups_categories_get) | **GET** /v1/organizations/groups/categories | Retrieves group categories with pagination.
[**v1_organizations_groups_categories_id_get**](OrganizationsApi.md#v1_organizations_groups_categories_id_get) | **GET** /v1/organizations/groups/categories/{id} | Retrieves group category with given identifier.
[**v1_organizations_groups_get**](OrganizationsApi.md#v1_organizations_groups_get) | **GET** /v1/organizations/groups | Retrieves groups with pagination.
[**v1_organizations_groups_id_affiliated_people_get**](OrganizationsApi.md#v1_organizations_groups_id_affiliated_people_get) | **GET** /v1/organizations/groups/{id}/affiliatedPeople | Retrieves group-people relation for given group.
[**v1_organizations_groups_id_get**](OrganizationsApi.md#v1_organizations_groups_id_get) | **GET** /v1/organizations/groups/{id} | Retrieves a group with given identifier.
[**v1_organizations_groups_person_id_get**](OrganizationsApi.md#v1_organizations_groups_person_id_get) | **GET** /v1/organizations/groups/person/{id} | Retrieves groups identifiers where given person affiliates.
[**v1_organizations_hierarchy_get**](OrganizationsApi.md#v1_organizations_hierarchy_get) | **GET** /v1/organizations/hierarchy | Retrieves organization hierarchy.
[**v1_organizations_id_get**](OrganizationsApi.md#v1_organizations_id_get) | **GET** /v1/organizations/{id} | Retrieves an organization with given identifier.


# **v1_organizations_get**
> List[Organization] v1_organizations_get(page=page, page_size=page_size)

Retrieves organizations with pagination.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.organization import Organization
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
    api_instance = simployer_client.OrganizationsApi(api_client)
    page = 1 # int | Page number (default is 1). (optional) (default to 1)
    page_size = 100 # int | Number of items per page (default is 100). (optional) (default to 100)

    try:
        # Retrieves organizations with pagination.
        api_response = api_instance.v1_organizations_get(page=page, page_size=page_size)
        print("The response of OrganizationsApi->v1_organizations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->v1_organizations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number (default is 1). | [optional] [default to 1]
 **page_size** | **int**| Number of items per page (default is 100). | [optional] [default to 100]

### Return type

[**List[Organization]**](Organization.md)

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

# **v1_organizations_groups_affiliated_people_get**
> List[GroupPeopleRelations] v1_organizations_groups_affiliated_people_get(page=page, page_size=page_size)

Retrieves group-people relations with pagination.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.group_people_relations import GroupPeopleRelations
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
    api_instance = simployer_client.OrganizationsApi(api_client)
    page = 1 # int | Page number (default is 1). (optional) (default to 1)
    page_size = 100 # int | Number of items per page (default is 100). (optional) (default to 100)

    try:
        # Retrieves group-people relations with pagination.
        api_response = api_instance.v1_organizations_groups_affiliated_people_get(page=page, page_size=page_size)
        print("The response of OrganizationsApi->v1_organizations_groups_affiliated_people_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->v1_organizations_groups_affiliated_people_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number (default is 1). | [optional] [default to 1]
 **page_size** | **int**| Number of items per page (default is 100). | [optional] [default to 100]

### Return type

[**List[GroupPeopleRelations]**](GroupPeopleRelations.md)

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

# **v1_organizations_groups_categories_get**
> List[GroupCategory] v1_organizations_groups_categories_get(page=page, page_size=page_size)

Retrieves group categories with pagination.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.group_category import GroupCategory
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
    api_instance = simployer_client.OrganizationsApi(api_client)
    page = 1 # int | Page number (default is 1). (optional) (default to 1)
    page_size = 100 # int | Number of items per page (default is 100). (optional) (default to 100)

    try:
        # Retrieves group categories with pagination.
        api_response = api_instance.v1_organizations_groups_categories_get(page=page, page_size=page_size)
        print("The response of OrganizationsApi->v1_organizations_groups_categories_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->v1_organizations_groups_categories_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number (default is 1). | [optional] [default to 1]
 **page_size** | **int**| Number of items per page (default is 100). | [optional] [default to 100]

### Return type

[**List[GroupCategory]**](GroupCategory.md)

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

# **v1_organizations_groups_categories_id_get**
> GroupCategory v1_organizations_groups_categories_id_get(id)

Retrieves group category with given identifier.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.group_category import GroupCategory
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
    api_instance = simployer_client.OrganizationsApi(api_client)
    id = 'id_example' # str | Identifier of a group category.

    try:
        # Retrieves group category with given identifier.
        api_response = api_instance.v1_organizations_groups_categories_id_get(id)
        print("The response of OrganizationsApi->v1_organizations_groups_categories_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->v1_organizations_groups_categories_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a group category. | 

### Return type

[**GroupCategory**](GroupCategory.md)

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

# **v1_organizations_groups_get**
> List[Group] v1_organizations_groups_get(page=page, page_size=page_size)

Retrieves groups with pagination.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.group import Group
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
    api_instance = simployer_client.OrganizationsApi(api_client)
    page = 1 # int | Page number (default is 1). (optional) (default to 1)
    page_size = 100 # int | Number of items per page (default is 100). (optional) (default to 100)

    try:
        # Retrieves groups with pagination.
        api_response = api_instance.v1_organizations_groups_get(page=page, page_size=page_size)
        print("The response of OrganizationsApi->v1_organizations_groups_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->v1_organizations_groups_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number (default is 1). | [optional] [default to 1]
 **page_size** | **int**| Number of items per page (default is 100). | [optional] [default to 100]

### Return type

[**List[Group]**](Group.md)

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

# **v1_organizations_groups_id_affiliated_people_get**
> GroupPeopleRelations v1_organizations_groups_id_affiliated_people_get(id)

Retrieves group-people relation for given group.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.group_people_relations import GroupPeopleRelations
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
    api_instance = simployer_client.OrganizationsApi(api_client)
    id = 'id_example' # str | Identifier of group.

    try:
        # Retrieves group-people relation for given group.
        api_response = api_instance.v1_organizations_groups_id_affiliated_people_get(id)
        print("The response of OrganizationsApi->v1_organizations_groups_id_affiliated_people_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->v1_organizations_groups_id_affiliated_people_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of group. | 

### Return type

[**GroupPeopleRelations**](GroupPeopleRelations.md)

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

# **v1_organizations_groups_id_get**
> Group v1_organizations_groups_id_get(id)

Retrieves a group with given identifier.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.group import Group
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
    api_instance = simployer_client.OrganizationsApi(api_client)
    id = 'id_example' # str | Identifier of group.

    try:
        # Retrieves a group with given identifier.
        api_response = api_instance.v1_organizations_groups_id_get(id)
        print("The response of OrganizationsApi->v1_organizations_groups_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->v1_organizations_groups_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of group. | 

### Return type

[**Group**](Group.md)

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

# **v1_organizations_groups_person_id_get**
> List[str] v1_organizations_groups_person_id_get(id)

Retrieves groups identifiers where given person affiliates.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
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
    api_instance = simployer_client.OrganizationsApi(api_client)
    id = 'id_example' # str | Identifier of person.

    try:
        # Retrieves groups identifiers where given person affiliates.
        api_response = api_instance.v1_organizations_groups_person_id_get(id)
        print("The response of OrganizationsApi->v1_organizations_groups_person_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->v1_organizations_groups_person_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of person. | 

### Return type

**List[str]**

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

# **v1_organizations_hierarchy_get**
> OrganizationHierarchy v1_organizations_hierarchy_get()

Retrieves organization hierarchy.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.organization_hierarchy import OrganizationHierarchy
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
    api_instance = simployer_client.OrganizationsApi(api_client)

    try:
        # Retrieves organization hierarchy.
        api_response = api_instance.v1_organizations_hierarchy_get()
        print("The response of OrganizationsApi->v1_organizations_hierarchy_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->v1_organizations_hierarchy_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OrganizationHierarchy**](OrganizationHierarchy.md)

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

# **v1_organizations_id_get**
> Organization v1_organizations_id_get(id)

Retrieves an organization with given identifier.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.organization import Organization
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
    api_instance = simployer_client.OrganizationsApi(api_client)
    id = 'id_example' # str | Identifier of organization.

    try:
        # Retrieves an organization with given identifier.
        api_response = api_instance.v1_organizations_id_get(id)
        print("The response of OrganizationsApi->v1_organizations_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->v1_organizations_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of organization. | 

### Return type

[**Organization**](Organization.md)

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


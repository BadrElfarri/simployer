# simployer_client.EmploymentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_employments_contracts_get**](EmploymentsApi.md#v1_employments_contracts_get) | **GET** /v1/employments/contracts | Retrieves contracts with pagination.
[**v1_employments_contracts_id_get**](EmploymentsApi.md#v1_employments_contracts_id_get) | **GET** /v1/employments/contracts/{id} | Retrieves the contract with given identifier.
[**v1_employments_contracts_person_id_get**](EmploymentsApi.md#v1_employments_contracts_person_id_get) | **GET** /v1/employments/contracts/person/{id} | Retrieves the contracts associated with person.
[**v1_employments_employee_id_get**](EmploymentsApi.md#v1_employments_employee_id_get) | **GET** /v1/employments/employee/{id} | Retrieves employments for given employee.
[**v1_employments_get**](EmploymentsApi.md#v1_employments_get) | **GET** /v1/employments | Retrieves employments with pagination.
[**v1_employments_id_get**](EmploymentsApi.md#v1_employments_id_get) | **GET** /v1/employments/{id} | Retrieves employments with given identifier.
[**v1_employments_person_id_get**](EmploymentsApi.md#v1_employments_person_id_get) | **GET** /v1/employments/person/{id} | Retrieves employments for given person.
[**v1_employments_salaries_employment_id_get**](EmploymentsApi.md#v1_employments_salaries_employment_id_get) | **GET** /v1/employments/salaries/employment/{id} | Retrieves salary for given employment.
[**v1_employments_salaries_get**](EmploymentsApi.md#v1_employments_salaries_get) | **GET** /v1/employments/salaries | Retrieves salaries with pagination.
[**v1_employments_salaries_person_id_get**](EmploymentsApi.md#v1_employments_salaries_person_id_get) | **GET** /v1/employments/salaries/person/{id} | Retrieves salaries for given person.
[**v1_employments_termination_causes_get**](EmploymentsApi.md#v1_employments_termination_causes_get) | **GET** /v1/employments/terminationCauses | Retrieves termination causes with pagination.
[**v1_employments_termination_causes_id_get**](EmploymentsApi.md#v1_employments_termination_causes_id_get) | **GET** /v1/employments/terminationCauses/{id} | Retrieves termination cause with given identifier.


# **v1_employments_contracts_get**
> List[Contract] v1_employments_contracts_get(page=page, page_size=page_size)

Retrieves contracts with pagination.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.contract import Contract
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
    api_instance = simployer_client.EmploymentsApi(api_client)
    page = 1 # int | Page number (default is 1). (optional) (default to 1)
    page_size = 100 # int | Number of items per page (default is 100). (optional) (default to 100)

    try:
        # Retrieves contracts with pagination.
        api_response = api_instance.v1_employments_contracts_get(page=page, page_size=page_size)
        print("The response of EmploymentsApi->v1_employments_contracts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmploymentsApi->v1_employments_contracts_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number (default is 1). | [optional] [default to 1]
 **page_size** | **int**| Number of items per page (default is 100). | [optional] [default to 100]

### Return type

[**List[Contract]**](Contract.md)

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

# **v1_employments_contracts_id_get**
> Contract v1_employments_contracts_id_get(id)

Retrieves the contract with given identifier.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.contract import Contract
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
    api_instance = simployer_client.EmploymentsApi(api_client)
    id = 'id_example' # str | Identifier of contract.

    try:
        # Retrieves the contract with given identifier.
        api_response = api_instance.v1_employments_contracts_id_get(id)
        print("The response of EmploymentsApi->v1_employments_contracts_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmploymentsApi->v1_employments_contracts_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of contract. | 

### Return type

[**Contract**](Contract.md)

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

# **v1_employments_contracts_person_id_get**
> List[Contract] v1_employments_contracts_person_id_get(id)

Retrieves the contracts associated with person.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.contract import Contract
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
    api_instance = simployer_client.EmploymentsApi(api_client)
    id = 'id_example' # str | Identifier of person.

    try:
        # Retrieves the contracts associated with person.
        api_response = api_instance.v1_employments_contracts_person_id_get(id)
        print("The response of EmploymentsApi->v1_employments_contracts_person_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmploymentsApi->v1_employments_contracts_person_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of person. | 

### Return type

[**List[Contract]**](Contract.md)

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

# **v1_employments_employee_id_get**
> List[Employment] v1_employments_employee_id_get(id)

Retrieves employments for given employee.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.employment import Employment
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
    api_instance = simployer_client.EmploymentsApi(api_client)
    id = 'id_example' # str | Identifier of employee associated with employments.

    try:
        # Retrieves employments for given employee.
        api_response = api_instance.v1_employments_employee_id_get(id)
        print("The response of EmploymentsApi->v1_employments_employee_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmploymentsApi->v1_employments_employee_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of employee associated with employments. | 

### Return type

[**List[Employment]**](Employment.md)

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

# **v1_employments_get**
> List[Employment] v1_employments_get(page=page, page_size=page_size)

Retrieves employments with pagination.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.employment import Employment
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
    api_instance = simployer_client.EmploymentsApi(api_client)
    page = 1 # int | Page number (default is 1). (optional) (default to 1)
    page_size = 100 # int | Number of items per page (default is 100). (optional) (default to 100)

    try:
        # Retrieves employments with pagination.
        api_response = api_instance.v1_employments_get(page=page, page_size=page_size)
        print("The response of EmploymentsApi->v1_employments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmploymentsApi->v1_employments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number (default is 1). | [optional] [default to 1]
 **page_size** | **int**| Number of items per page (default is 100). | [optional] [default to 100]

### Return type

[**List[Employment]**](Employment.md)

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

# **v1_employments_id_get**
> Employment v1_employments_id_get(id)

Retrieves employments with given identifier.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.employment import Employment
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
    api_instance = simployer_client.EmploymentsApi(api_client)
    id = 'id_example' # str | Identifier of employment.

    try:
        # Retrieves employments with given identifier.
        api_response = api_instance.v1_employments_id_get(id)
        print("The response of EmploymentsApi->v1_employments_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmploymentsApi->v1_employments_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of employment. | 

### Return type

[**Employment**](Employment.md)

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

# **v1_employments_person_id_get**
> List[Employment] v1_employments_person_id_get(id)

Retrieves employments for given person.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.employment import Employment
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
    api_instance = simployer_client.EmploymentsApi(api_client)
    id = 'id_example' # str | Identifier of person associated with employments.

    try:
        # Retrieves employments for given person.
        api_response = api_instance.v1_employments_person_id_get(id)
        print("The response of EmploymentsApi->v1_employments_person_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmploymentsApi->v1_employments_person_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of person associated with employments. | 

### Return type

[**List[Employment]**](Employment.md)

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

# **v1_employments_salaries_employment_id_get**
> Salary v1_employments_salaries_employment_id_get(id, period_type=period_type)

Retrieves salary for given employment.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.period_type import PeriodType
from simployer_client.models.salary import Salary
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
    api_instance = simployer_client.EmploymentsApi(api_client)
    id = 'id_example' # str | Identifier of employment associated with salary.
    period_type = simployer_client.PeriodType() # PeriodType | Parameter to set for which period salaries will be presented (default is yearly). (optional)

    try:
        # Retrieves salary for given employment.
        api_response = api_instance.v1_employments_salaries_employment_id_get(id, period_type=period_type)
        print("The response of EmploymentsApi->v1_employments_salaries_employment_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmploymentsApi->v1_employments_salaries_employment_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of employment associated with salary. | 
 **period_type** | [**PeriodType**](.md)| Parameter to set for which period salaries will be presented (default is yearly). | [optional] 

### Return type

[**Salary**](Salary.md)

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

# **v1_employments_salaries_get**
> List[Salary] v1_employments_salaries_get(current_salary_only=current_salary_only, period_type=period_type, page=page, page_size=page_size)

Retrieves salaries with pagination.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.period_type import PeriodType
from simployer_client.models.salary import Salary
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
    api_instance = simployer_client.EmploymentsApi(api_client)
    current_salary_only = True # bool | Flag to indicate if only current salaries should be retrieved (default is true). (optional) (default to True)
    period_type = simployer_client.PeriodType() # PeriodType | Parameter to set for which period salaries will be presented (default is yearly). (optional)
    page = 1 # int | Page number (default is 1). (optional) (default to 1)
    page_size = 100 # int | Number of items per page (default is 100). (optional) (default to 100)

    try:
        # Retrieves salaries with pagination.
        api_response = api_instance.v1_employments_salaries_get(current_salary_only=current_salary_only, period_type=period_type, page=page, page_size=page_size)
        print("The response of EmploymentsApi->v1_employments_salaries_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmploymentsApi->v1_employments_salaries_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **current_salary_only** | **bool**| Flag to indicate if only current salaries should be retrieved (default is true). | [optional] [default to True]
 **period_type** | [**PeriodType**](.md)| Parameter to set for which period salaries will be presented (default is yearly). | [optional] 
 **page** | **int**| Page number (default is 1). | [optional] [default to 1]
 **page_size** | **int**| Number of items per page (default is 100). | [optional] [default to 100]

### Return type

[**List[Salary]**](Salary.md)

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

# **v1_employments_salaries_person_id_get**
> List[Salary] v1_employments_salaries_person_id_get(id, current_salary_only=current_salary_only, period_type=period_type)

Retrieves salaries for given person.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.period_type import PeriodType
from simployer_client.models.salary import Salary
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
    api_instance = simployer_client.EmploymentsApi(api_client)
    id = 'id_example' # str | Identifier of person associated with salaries.
    current_salary_only = True # bool | Flag to indicate if only current salaries should be retrieved (default is true). (optional) (default to True)
    period_type = simployer_client.PeriodType() # PeriodType | Parameter to set for which period salaries will be presented (default is yearly). (optional)

    try:
        # Retrieves salaries for given person.
        api_response = api_instance.v1_employments_salaries_person_id_get(id, current_salary_only=current_salary_only, period_type=period_type)
        print("The response of EmploymentsApi->v1_employments_salaries_person_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmploymentsApi->v1_employments_salaries_person_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of person associated with salaries. | 
 **current_salary_only** | **bool**| Flag to indicate if only current salaries should be retrieved (default is true). | [optional] [default to True]
 **period_type** | [**PeriodType**](.md)| Parameter to set for which period salaries will be presented (default is yearly). | [optional] 

### Return type

[**List[Salary]**](Salary.md)

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

# **v1_employments_termination_causes_get**
> List[TerminationCause] v1_employments_termination_causes_get(page=page, page_size=page_size)

Retrieves termination causes with pagination.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.termination_cause import TerminationCause
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
    api_instance = simployer_client.EmploymentsApi(api_client)
    page = 1 # int | Page number (default is 1). (optional) (default to 1)
    page_size = 100 # int | Number of items per page (default is 100). (optional) (default to 100)

    try:
        # Retrieves termination causes with pagination.
        api_response = api_instance.v1_employments_termination_causes_get(page=page, page_size=page_size)
        print("The response of EmploymentsApi->v1_employments_termination_causes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmploymentsApi->v1_employments_termination_causes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number (default is 1). | [optional] [default to 1]
 **page_size** | **int**| Number of items per page (default is 100). | [optional] [default to 100]

### Return type

[**List[TerminationCause]**](TerminationCause.md)

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

# **v1_employments_termination_causes_id_get**
> TerminationCause v1_employments_termination_causes_id_get(id)

Retrieves termination cause with given identifier.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.termination_cause import TerminationCause
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
    api_instance = simployer_client.EmploymentsApi(api_client)
    id = 'id_example' # str | Identifier of termination cause.

    try:
        # Retrieves termination cause with given identifier.
        api_response = api_instance.v1_employments_termination_causes_id_get(id)
        print("The response of EmploymentsApi->v1_employments_termination_causes_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmploymentsApi->v1_employments_termination_causes_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of termination cause. | 

### Return type

[**TerminationCause**](TerminationCause.md)

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


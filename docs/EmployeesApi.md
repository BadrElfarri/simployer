# simployer_client.EmployeesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_employees_get**](EmployeesApi.md#v1_employees_get) | **GET** /v1/employees | Retrieves employees with pagination.


# **v1_employees_get**
> List[Employee] v1_employees_get(page=page, page_size=page_size)

Retrieves employees with pagination.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.employee import Employee
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
    api_instance = simployer_client.EmployeesApi(api_client)
    page = 1 # int | Page number (default is 1). (optional) (default to 1)
    page_size = 100 # int | Number of items per page (default is 100). (optional) (default to 100)

    try:
        # Retrieves employees with pagination.
        api_response = api_instance.v1_employees_get(page=page, page_size=page_size)
        print("The response of EmployeesApi->v1_employees_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->v1_employees_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number (default is 1). | [optional] [default to 1]
 **page_size** | **int**| Number of items per page (default is 100). | [optional] [default to 100]

### Return type

[**List[Employee]**](Employee.md)

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


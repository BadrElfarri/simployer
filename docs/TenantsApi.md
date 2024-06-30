# simployer_client.TenantsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_tenants_get**](TenantsApi.md#v1_tenants_get) | **GET** /v1/tenants | Retrieves the tenant information.


# **v1_tenants_get**
> Tenant v1_tenants_get()

Retrieves the tenant information.

### Example

* Api Key Authentication (Bearer):

```python
import simployer_client
from simployer_client.models.tenant import Tenant
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
    api_instance = simployer_client.TenantsApi(api_client)

    try:
        # Retrieves the tenant information.
        api_response = api_instance.v1_tenants_get()
        print("The response of TenantsApi->v1_tenants_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsApi->v1_tenants_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Tenant**](Tenant.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


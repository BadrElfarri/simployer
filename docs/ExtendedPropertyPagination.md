# ExtendedPropertyPagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**records** | [**List[ExtendedProperty]**](ExtendedProperty.md) |  | [optional] 

## Example

```python
from simployer_client.models.extended_property_pagination import ExtendedPropertyPagination

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendedPropertyPagination from a JSON string
extended_property_pagination_instance = ExtendedPropertyPagination.from_json(json)
# print the JSON string representation of the object
print(ExtendedPropertyPagination.to_json())

# convert the object into a dict
extended_property_pagination_dict = extended_property_pagination_instance.to_dict()
# create an instance of ExtendedPropertyPagination from a dict
extended_property_pagination_from_dict = ExtendedPropertyPagination.from_dict(extended_property_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



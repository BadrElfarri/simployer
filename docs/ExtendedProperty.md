# ExtendedProperty

Represents an extended property associated with a person.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**person_id** | **str** | Unique identifier of the person associated with this extended property. | [optional] 
**property_type_id** | **str** | Unique identifier of the property type. | [optional] 
**property_value_id** | **str** | Unique identifier of the property value. | [optional] 
**property_type** | **str** | Type of the extended property. | [optional] 
**property_value** | **str** | Value of the extended property. | [optional] 

## Example

```python
from simployer_client.models.extended_property import ExtendedProperty

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendedProperty from a JSON string
extended_property_instance = ExtendedProperty.from_json(json)
# print the JSON string representation of the object
print(ExtendedProperty.to_json())

# convert the object into a dict
extended_property_dict = extended_property_instance.to_dict()
# create an instance of ExtendedProperty from a dict
extended_property_from_dict = ExtendedProperty.from_dict(extended_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



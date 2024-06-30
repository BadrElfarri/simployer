# Phone


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the phone | [optional] 
**unit_id** | **str** | Unique identifier of the unit associated with this phone | [optional] 
**unit_type** | [**UnitType**](UnitType.md) |  | [optional] 
**type** | [**PhoneType**](PhoneType.md) |  | [optional] 
**number** | **str** | Phone number | [optional] 

## Example

```python
from simployer_client.models.phone import Phone

# TODO update the JSON string below
json = "{}"
# create an instance of Phone from a JSON string
phone_instance = Phone.from_json(json)
# print the JSON string representation of the object
print(Phone.to_json())

# convert the object into a dict
phone_dict = phone_instance.to_dict()
# create an instance of Phone from a dict
phone_from_dict = Phone.from_dict(phone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



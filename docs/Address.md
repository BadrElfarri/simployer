# Address


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the Address | [optional] 
**unit_id** | **str** | Unique identifier of the unit that address belongs to | [optional] 
**unit_type** | [**UnitType**](UnitType.md) |  | [optional] 
**type** | [**AddressType**](AddressType.md) |  | [optional] 
**country** | [**CountryType**](CountryType.md) |  | [optional] 
**street_name1** | **str** | First line of the address | [optional] 
**street_name2** | **str** | Second line of the address | [optional] 
**street_name3** | **str** | Third line of the address | [optional] 
**postal_code** | **str** | Post code | [optional] 
**postal_place** | **str** | City | [optional] 

## Example

```python
from simployer_client.models.address import Address

# TODO update the JSON string below
json = "{}"
# create an instance of Address from a JSON string
address_instance = Address.from_json(json)
# print the JSON string representation of the object
print(Address.to_json())

# convert the object into a dict
address_dict = address_instance.to_dict()
# create an instance of Address from a dict
address_from_dict = Address.from_dict(address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



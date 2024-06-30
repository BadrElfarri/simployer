# ElectronicAddress

Represents an electronic address.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the electronic address. | [optional] 
**unit_id** | **str** | Unique identifier of the unit associated with this electronic address. | [optional] 
**unit_type** | [**UnitType**](UnitType.md) |  | [optional] 
**type** | [**ElectronicAddressType**](ElectronicAddressType.md) |  | [optional] 
**address** | **str** | Address value. | [optional] 

## Example

```python
from simployer_client.models.electronic_address import ElectronicAddress

# TODO update the JSON string below
json = "{}"
# create an instance of ElectronicAddress from a JSON string
electronic_address_instance = ElectronicAddress.from_json(json)
# print the JSON string representation of the object
print(ElectronicAddress.to_json())

# convert the object into a dict
electronic_address_dict = electronic_address_instance.to_dict()
# create an instance of ElectronicAddress from a dict
electronic_address_from_dict = ElectronicAddress.from_dict(electronic_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



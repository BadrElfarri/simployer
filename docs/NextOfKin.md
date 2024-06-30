# NextOfKin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the next of kin. | [optional] 
**relative_id** | **str** | Unique identifier of the relative associated with the next of kin. | [optional] 
**name** | **str** | Name of the next of kin. | [optional] 
**relation** | **str** | Relationship of the next of kin to the individual. | [optional] 
**email** | **str** | Email address of the next of kin. | [optional] 
**phone_number** | **str** | Phone number of the next of kin. | [optional] 
**country** | [**CountryType**](CountryType.md) |  | [optional] 
**street_name1** | **str** | First line of the address | [optional] 
**street_name2** | **str** | Second line of the address | [optional] 
**street_name3** | **str** | Third line of the address | [optional] 
**postal_code** | **str** | Post code | [optional] 
**postal_place** | **str** | City | [optional] 

## Example

```python
from simployer_client.models.next_of_kin import NextOfKin

# TODO update the JSON string below
json = "{}"
# create an instance of NextOfKin from a JSON string
next_of_kin_instance = NextOfKin.from_json(json)
# print the JSON string representation of the object
print(NextOfKin.to_json())

# convert the object into a dict
next_of_kin_dict = next_of_kin_instance.to_dict()
# create an instance of NextOfKin from a dict
next_of_kin_from_dict = NextOfKin.from_dict(next_of_kin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



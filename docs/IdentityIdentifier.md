# IdentityIdentifier

Represents an identity identifier associated with a person.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of this identity identifier. | [optional] 
**value** | **str** | Value of the identity identifier. | [optional] 
**type** | [**PersonIdentityIdentifierType**](PersonIdentityIdentifierType.md) |  | [optional] 
**country** | [**CountryType**](CountryType.md) |  | [optional] 
**person_id** | **str** | The unique identifier of the person associated with this identity identifier. | [optional] 

## Example

```python
from simployer_client.models.identity_identifier import IdentityIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityIdentifier from a JSON string
identity_identifier_instance = IdentityIdentifier.from_json(json)
# print the JSON string representation of the object
print(IdentityIdentifier.to_json())

# convert the object into a dict
identity_identifier_dict = identity_identifier_instance.to_dict()
# create an instance of IdentityIdentifier from a dict
identity_identifier_from_dict = IdentityIdentifier.from_dict(identity_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



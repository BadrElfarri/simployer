# Person

Represents a person.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the person. | [optional] 
**first_name** | **str** | First name of the person. | [optional] 
**last_name** | **str** | Last name of the person. | [optional] 
**nick_name** | **str** | Nickname of the person. | [optional] 
**birthdate** | **datetime** | Birthdate of the person. | [optional] 
**seniority_date** | **datetime** | Date indicating the seniority or length of service. | [optional] 
**bank_account1** | **str** | First bank account number. | [optional] 
**iban1** | **str** | International Bank Account Number (IBAN) associated with the first bank account. | [optional] 
**bank_account2** | **str** | Second bank account number. | [optional] 
**iban2** | **str** | International Bank Account Number (IBAN) associated with the second bank account. | [optional] 
**bank_country1** | [**CountryType**](CountryType.md) |  | [optional] 
**bank_country2** | [**CountryType**](CountryType.md) |  | [optional] 
**sex** | [**SexType**](SexType.md) |  | [optional] 
**nationality** | [**CountryType**](CountryType.md) |  | [optional] 
**active** | **bool** | Indicates if the person is active. | [optional] [readonly] 
**affiliated_organization_id** | **str** | Affiliated organization identifier of the person. | [optional] [readonly] 
**primary_phone** | **str** | Primary phone number of the person. | [optional] 
**primary_email** | **str** | Primary email address of the person. | [optional] 

## Example

```python
from simployer_client.models.person import Person

# TODO update the JSON string below
json = "{}"
# create an instance of Person from a JSON string
person_instance = Person.from_json(json)
# print the JSON string representation of the object
print(Person.to_json())

# convert the object into a dict
person_dict = person_instance.to_dict()
# create an instance of Person from a dict
person_from_dict = Person.from_dict(person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



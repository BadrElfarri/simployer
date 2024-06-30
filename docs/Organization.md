# Organization

Represents an organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of the organization. | [optional] 
**sub_type** | [**OrganizationUnitType**](OrganizationUnitType.md) |  | [optional] 
**name** | **str** | Name of the organization. | [optional] 
**company_number** | **str** | Company number. | [optional] 
**active** | **bool** | Indicates if the organization is active. | [optional] 
**department_code** | **str** | Department code of the organization. | [optional] 
**manager_id** | **str** | Manager&#39;s identifier of the organization. | [optional] 
**parent_organization_id** | **str** | Parent organization identifier. | [optional] [readonly] 
**organization_number** | **str** | Organization number. | [optional] 
**nace** | **str** | NACE (Nomenclature of Economic Activities) code. | [optional] 
**system_country** | [**CountryType**](CountryType.md) |  | [optional] 
**system_organization_currency** | [**OrganizationCurrencyType**](OrganizationCurrencyType.md) |  | [optional] 

## Example

```python
from simployer_client.models.organization import Organization

# TODO update the JSON string below
json = "{}"
# create an instance of Organization from a JSON string
organization_instance = Organization.from_json(json)
# print the JSON string representation of the object
print(Organization.to_json())

# convert the object into a dict
organization_dict = organization_instance.to_dict()
# create an instance of Organization from a dict
organization_from_dict = Organization.from_dict(organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



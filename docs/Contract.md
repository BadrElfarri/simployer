# Contract

Represents a contract.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of the contract. | [optional] 
**name** | **str** | Name of the contract. | [optional] 
**type** | [**ContractType**](ContractType.md) |  | [optional] 
**status** | [**AgreementStatus**](AgreementStatus.md) |  | [optional] 
**signature_type** | [**SignatureTypeEnum**](SignatureTypeEnum.md) |  | [optional] 
**from_date** | **datetime** | Start date of the contract. | [optional] 
**to_date** | **datetime** | End date of the contract. | [optional] 
**person_id** | **str** | Identifier of the person associated with the contract. | [optional] 
**person_name** | **str** | Name of the person associated with the contract. | [optional] 
**employment_id** | **str** | Identifier of the employment associated with the contract. | [optional] [readonly] 

## Example

```python
from simployer_client.models.contract import Contract

# TODO update the JSON string below
json = "{}"
# create an instance of Contract from a JSON string
contract_instance = Contract.from_json(json)
# print the JSON string representation of the object
print(Contract.to_json())

# convert the object into a dict
contract_dict = contract_instance.to_dict()
# create an instance of Contract from a dict
contract_from_dict = Contract.from_dict(contract_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TerminationCause

Represents a termination cause.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of the termination cause. | [optional] 
**name** | **str** | Name of the termination cause. | [optional] 
**description** | **str** | Description of the termination cause. | [optional] 
**code** | **str** | Code of the termination cause. | [optional] 
**is_system** | **bool** | Indicates if the termination cause is a system-defined cause. | [optional] 
**active** | **bool** | Indicates if the termination cause is active. | [optional] [readonly] 

## Example

```python
from simployer_client.models.termination_cause import TerminationCause

# TODO update the JSON string below
json = "{}"
# create an instance of TerminationCause from a JSON string
termination_cause_instance = TerminationCause.from_json(json)
# print the JSON string representation of the object
print(TerminationCause.to_json())

# convert the object into a dict
termination_cause_dict = termination_cause_instance.to_dict()
# create an instance of TerminationCause from a dict
termination_cause_from_dict = TerminationCause.from_dict(termination_cause_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



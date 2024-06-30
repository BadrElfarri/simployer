# PersonManagerRelationship

Represents the relationship between a person and their manager.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**person_name** | **str** | Name of the person. | [optional] 
**person_id** | **str** | Identifier of the person. | [optional] [readonly] 
**manager_name** | **str** | Name of the manager. | [optional] 
**manager_id** | **str** | Identifier of the manager. | [optional] [readonly] 
**is_specified_manager** | **bool** | Indicates if the manager is specified. | [optional] [readonly] 
**last_changed** | **datetime** | Date when the relationship was last changed. | [optional] 

## Example

```python
from simployer_client.models.person_manager_relationship import PersonManagerRelationship

# TODO update the JSON string below
json = "{}"
# create an instance of PersonManagerRelationship from a JSON string
person_manager_relationship_instance = PersonManagerRelationship.from_json(json)
# print the JSON string representation of the object
print(PersonManagerRelationship.to_json())

# convert the object into a dict
person_manager_relationship_dict = person_manager_relationship_instance.to_dict()
# create an instance of PersonManagerRelationship from a dict
person_manager_relationship_from_dict = PersonManagerRelationship.from_dict(person_manager_relationship_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



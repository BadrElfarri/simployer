# GroupPeopleRelations

Represents the relations between people and managers in a group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of the group. | [optional] [readonly] 
**people** | **List[str]** | People in the group. | [optional] 
**managers** | **List[str]** | Managers in the group. | [optional] 

## Example

```python
from simployer_client.models.group_people_relations import GroupPeopleRelations

# TODO update the JSON string below
json = "{}"
# create an instance of GroupPeopleRelations from a JSON string
group_people_relations_instance = GroupPeopleRelations.from_json(json)
# print the JSON string representation of the object
print(GroupPeopleRelations.to_json())

# convert the object into a dict
group_people_relations_dict = group_people_relations_instance.to_dict()
# create an instance of GroupPeopleRelations from a dict
group_people_relations_from_dict = GroupPeopleRelations.from_dict(group_people_relations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



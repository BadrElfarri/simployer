# Group

Represents a group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the group. | [optional] 
**name** | **str** | Name of the group. | [optional] 
**description** | **str** | Description of the group. | [optional] 
**category** | **str** | Category of the group. | [optional] 
**code** | **str** | Code of the group. | [optional] 
**managers** | [**List[GroupManager]**](GroupManager.md) | Managers of the group. | [optional] 

## Example

```python
from simployer_client.models.group import Group

# TODO update the JSON string below
json = "{}"
# create an instance of Group from a JSON string
group_instance = Group.from_json(json)
# print the JSON string representation of the object
print(Group.to_json())

# convert the object into a dict
group_dict = group_instance.to_dict()
# create an instance of Group from a dict
group_from_dict = Group.from_dict(group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



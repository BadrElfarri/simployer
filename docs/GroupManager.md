# GroupManager

Represents a manager of a group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique Identifier of the manager. | [optional] [readonly] 
**name** | **str** | Name of the manager. | [optional] 

## Example

```python
from simployer_client.models.group_manager import GroupManager

# TODO update the JSON string below
json = "{}"
# create an instance of GroupManager from a JSON string
group_manager_instance = GroupManager.from_json(json)
# print the JSON string representation of the object
print(GroupManager.to_json())

# convert the object into a dict
group_manager_dict = group_manager_instance.to_dict()
# create an instance of GroupManager from a dict
group_manager_from_dict = GroupManager.from_dict(group_manager_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



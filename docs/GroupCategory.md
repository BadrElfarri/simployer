# GroupCategory

Represents the category of a group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the category. | [optional] [readonly] 
**code** | **str** | Code of the category. | [optional] 
**name** | **str** | Name of the category. | [optional] 
**description** | **str** | Description of the category. | [optional] 

## Example

```python
from simployer_client.models.group_category import GroupCategory

# TODO update the JSON string below
json = "{}"
# create an instance of GroupCategory from a JSON string
group_category_instance = GroupCategory.from_json(json)
# print the JSON string representation of the object
print(GroupCategory.to_json())

# convert the object into a dict
group_category_dict = group_category_instance.to_dict()
# create an instance of GroupCategory from a dict
group_category_from_dict = GroupCategory.from_dict(group_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



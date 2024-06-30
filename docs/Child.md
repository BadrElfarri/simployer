# Child


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the child. | [optional] 
**parent_id** | **str** | Unique identifier of the parent associated with the child. | [optional] 
**name** | **str** | Name of the child. | [optional] 
**active** | **bool** | Indicates whether the child is active. | [optional] 
**sex** | [**SexType**](SexType.md) |  | [optional] 
**birth_date** | **datetime** | Date of birth of the child. | [optional] 
**comment** | **str** | Additional comments about the child. | [optional] 
**split_care** | **bool** | Indicates whether the care of the child is split. | [optional] 
**split_care_percentage** | **int** | Percentage of split care for the child. | [optional] 
**lives_with_parent** | **bool** | Indicates whether the child lives with a parent. | [optional] 
**disabled_or_chronically_ill** | **bool** | Indicates whether the child is disabled or chronically ill. | [optional] 
**step_child** | **bool** | Indicates whether the child is a stepchild. | [optional] 

## Example

```python
from simployer_client.models.child import Child

# TODO update the JSON string below
json = "{}"
# create an instance of Child from a JSON string
child_instance = Child.from_json(json)
# print the JSON string representation of the object
print(Child.to_json())

# convert the object into a dict
child_dict = child_instance.to_dict()
# create an instance of Child from a dict
child_from_dict = Child.from_dict(child_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



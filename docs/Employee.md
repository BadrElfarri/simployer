# Employee

Represents an employee.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **str** | Unique identifier of the employee. | [optional] 
**person_id** | **str** | Identifier of the person. | [optional] 
**employee_company_id** | **str** | Unique identifier of the employee&#39;s company. | [optional] 
**employee_number** | **str** | Employee number | [optional] 

## Example

```python
from simployer_client.models.employee import Employee

# TODO update the JSON string below
json = "{}"
# create an instance of Employee from a JSON string
employee_instance = Employee.from_json(json)
# print the JSON string representation of the object
print(Employee.to_json())

# convert the object into a dict
employee_dict = employee_instance.to_dict()
# create an instance of Employee from a dict
employee_from_dict = Employee.from_dict(employee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Salary

Represents a salary.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employment_id** | **str** | Identifier of the employment associated with the salary. | [optional] 
**value** | **float** | Value of the salary. | [optional] 
**salary_currency_type** | [**SalaryCurrencyType**](SalaryCurrencyType.md) |  | [optional] 
**effective_date** | **datetime** | Effective date of the salary. | [optional] 
**employee_number** | **str** | Employee number associated with the salary. | [optional] 
**department_code** | **str** | Department code associated with the salary. | [optional] 
**employment_involvement_percent** | **float** | Percentage of employment involvement. | [optional] 

## Example

```python
from simployer_client.models.salary import Salary

# TODO update the JSON string below
json = "{}"
# create an instance of Salary from a JSON string
salary_instance = Salary.from_json(json)
# print the JSON string representation of the object
print(Salary.to_json())

# convert the object into a dict
salary_dict = salary_instance.to_dict()
# create an instance of Salary from a dict
salary_from_dict = Salary.from_dict(salary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



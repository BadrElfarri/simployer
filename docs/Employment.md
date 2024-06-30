# Employment

Represents an employment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**person_id** | **str** | Identifier of the person. | [optional] [readonly] 
**position_id** | **str** | Identifier of the position. | [optional] [readonly] 
**employment_id** | **str** | Identifier of the employment. | [optional] [readonly] 
**employment_company_id** | **str** | Identifier of the company associated with the employment. | [optional] [readonly] 
**termination_cause_id** | **str** | Identifier of the termination cause. | [optional] [readonly] 
**category_id** | **str** | Identifier of the category. | [optional] [readonly] 
**employee_id** | **str** | Identifier of the employee. | [optional] [readonly] 
**employee_company_id** | **str** | Identifier of the company associated with the employee. | [optional] [readonly] 
**start_date** | **datetime** | Start date of the employment. | [optional] 
**end_date** | **datetime** | End date of the employment. | [optional] 
**employee_number** | **str** | Employee number. | [optional] 
**assignment_type** | [**AssignmentUnitType**](AssignmentUnitType.md) |  | [optional] 
**assignment_value** | **float** | Assignment value. | [optional] 
**position_name** | **str** | Name of the position. | [optional] 
**position_number** | **int** | Number of the position. | [optional] 
**code** | **int** | Code. | [optional] 
**sub_code** | **int** | Sub code. | [optional] 
**category_name** | **str** | Name of the category. | [optional] 
**category_number** | **str** | Number of the category. | [optional] 
**category_hour_unit** | [**HourUnit**](HourUnit.md) |  | [optional] 
**category_hours_per_unit** | **float** | Hours per unit of the category. | [optional] 

## Example

```python
from simployer_client.models.employment import Employment

# TODO update the JSON string below
json = "{}"
# create an instance of Employment from a JSON string
employment_instance = Employment.from_json(json)
# print the JSON string representation of the object
print(Employment.to_json())

# convert the object into a dict
employment_dict = employment_instance.to_dict()
# create an instance of Employment from a dict
employment_from_dict = Employment.from_dict(employment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



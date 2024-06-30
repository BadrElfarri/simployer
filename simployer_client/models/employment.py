# coding: utf-8

"""
    HrConnect

    JWT token is required for authorization. Access to the API is granted through Simployer Admin Center: https://admincenter.simployer.com/    Endpoints with pagination support return following headers      x-has-next-page: True (indicates whether there are more records)      x-page: 1 (page numeration starts with 1)      x-page-size: 100 (records per page)      x-total-count: 120 (total number of records)      x-total-pages: 2 (total number of pages)

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from simployer_client.models.assignment_unit_type import AssignmentUnitType
from simployer_client.models.hour_unit import HourUnit
from typing import Optional, Set
from typing_extensions import Self

class Employment(BaseModel):
    """
    Represents an employment.
    """ # noqa: E501
    person_id: Optional[StrictStr] = Field(default=None, description="Identifier of the person.", alias="personId")
    position_id: Optional[StrictStr] = Field(default=None, description="Identifier of the position.", alias="positionId")
    employment_id: Optional[StrictStr] = Field(default=None, description="Identifier of the employment.", alias="employmentId")
    employment_company_id: Optional[StrictStr] = Field(default=None, description="Identifier of the company associated with the employment.", alias="employmentCompanyId")
    termination_cause_id: Optional[StrictStr] = Field(default=None, description="Identifier of the termination cause.", alias="terminationCauseId")
    category_id: Optional[StrictStr] = Field(default=None, description="Identifier of the category.", alias="categoryId")
    employee_id: Optional[StrictStr] = Field(default=None, description="Identifier of the employee.", alias="employeeId")
    employee_company_id: Optional[StrictStr] = Field(default=None, description="Identifier of the company associated with the employee.", alias="employeeCompanyId")
    start_date: Optional[datetime] = Field(default=None, description="Start date of the employment.", alias="startDate")
    end_date: Optional[datetime] = Field(default=None, description="End date of the employment.", alias="endDate")
    employee_number: Optional[StrictStr] = Field(default=None, description="Employee number.", alias="employeeNumber")
    assignment_type: Optional[AssignmentUnitType] = Field(default=None, alias="assignmentType")
    assignment_value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Assignment value.", alias="assignmentValue")
    position_name: Optional[StrictStr] = Field(default=None, description="Name of the position.", alias="positionName")
    position_number: Optional[StrictInt] = Field(default=None, description="Number of the position.", alias="positionNumber")
    code: Optional[StrictInt] = Field(default=None, description="Code.")
    sub_code: Optional[StrictInt] = Field(default=None, description="Sub code.", alias="subCode")
    category_name: Optional[StrictStr] = Field(default=None, description="Name of the category.", alias="categoryName")
    category_number: Optional[StrictStr] = Field(default=None, description="Number of the category.", alias="categoryNumber")
    category_hour_unit: Optional[HourUnit] = Field(default=None, alias="categoryHourUnit")
    category_hours_per_unit: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Hours per unit of the category.", alias="categoryHoursPerUnit")
    __properties: ClassVar[List[str]] = ["personId", "positionId", "employmentId", "employmentCompanyId", "terminationCauseId", "categoryId", "employeeId", "employeeCompanyId", "startDate", "endDate", "employeeNumber", "assignmentType", "assignmentValue", "positionName", "positionNumber", "code", "subCode", "categoryName", "categoryNumber", "categoryHourUnit", "categoryHoursPerUnit"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Employment from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "person_id",
            "position_id",
            "employment_id",
            "employment_company_id",
            "termination_cause_id",
            "category_id",
            "employee_id",
            "employee_company_id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if termination_cause_id (nullable) is None
        # and model_fields_set contains the field
        if self.termination_cause_id is None and "termination_cause_id" in self.model_fields_set:
            _dict['terminationCauseId'] = None

        # set to None if end_date (nullable) is None
        # and model_fields_set contains the field
        if self.end_date is None and "end_date" in self.model_fields_set:
            _dict['endDate'] = None

        # set to None if employee_number (nullable) is None
        # and model_fields_set contains the field
        if self.employee_number is None and "employee_number" in self.model_fields_set:
            _dict['employeeNumber'] = None

        # set to None if position_name (nullable) is None
        # and model_fields_set contains the field
        if self.position_name is None and "position_name" in self.model_fields_set:
            _dict['positionName'] = None

        # set to None if category_name (nullable) is None
        # and model_fields_set contains the field
        if self.category_name is None and "category_name" in self.model_fields_set:
            _dict['categoryName'] = None

        # set to None if category_number (nullable) is None
        # and model_fields_set contains the field
        if self.category_number is None and "category_number" in self.model_fields_set:
            _dict['categoryNumber'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Employment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "personId": obj.get("personId"),
            "positionId": obj.get("positionId"),
            "employmentId": obj.get("employmentId"),
            "employmentCompanyId": obj.get("employmentCompanyId"),
            "terminationCauseId": obj.get("terminationCauseId"),
            "categoryId": obj.get("categoryId"),
            "employeeId": obj.get("employeeId"),
            "employeeCompanyId": obj.get("employeeCompanyId"),
            "startDate": obj.get("startDate"),
            "endDate": obj.get("endDate"),
            "employeeNumber": obj.get("employeeNumber"),
            "assignmentType": obj.get("assignmentType"),
            "assignmentValue": obj.get("assignmentValue"),
            "positionName": obj.get("positionName"),
            "positionNumber": obj.get("positionNumber"),
            "code": obj.get("code"),
            "subCode": obj.get("subCode"),
            "categoryName": obj.get("categoryName"),
            "categoryNumber": obj.get("categoryNumber"),
            "categoryHourUnit": obj.get("categoryHourUnit"),
            "categoryHoursPerUnit": obj.get("categoryHoursPerUnit")
        })
        return _obj



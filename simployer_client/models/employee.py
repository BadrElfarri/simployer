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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Employee(BaseModel):
    """
    Represents an employee.
    """ # noqa: E501
    employee_id: Optional[StrictStr] = Field(default=None, description="Unique identifier of the employee.", alias="employeeId")
    person_id: Optional[StrictStr] = Field(default=None, description="Identifier of the person.", alias="personId")
    employee_company_id: Optional[StrictStr] = Field(default=None, description="Unique identifier of the employee's company.", alias="employeeCompanyId")
    employee_number: Optional[StrictStr] = Field(default=None, description="Employee number", alias="employeeNumber")
    __properties: ClassVar[List[str]] = ["employeeId", "personId", "employeeCompanyId", "employeeNumber"]

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
        """Create an instance of Employee from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if employee_number (nullable) is None
        # and model_fields_set contains the field
        if self.employee_number is None and "employee_number" in self.model_fields_set:
            _dict['employeeNumber'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Employee from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "employeeId": obj.get("employeeId"),
            "personId": obj.get("personId"),
            "employeeCompanyId": obj.get("employeeCompanyId"),
            "employeeNumber": obj.get("employeeNumber")
        })
        return _obj



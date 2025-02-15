# coding: utf-8

"""
    HrConnect

    JWT token is required for authorization. Access to the API is granted through Simployer Admin Center: https://admincenter.simployer.com/    Endpoints with pagination support return following headers      x-has-next-page: True (indicates whether there are more records)      x-page: 1 (page numeration starts with 1)      x-page-size: 100 (records per page)      x-total-count: 120 (total number of records)      x-total-pages: 2 (total number of pages)

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class AddressType(str, Enum):
    """
    Type of the address
    """

    """
    allowed enum values
    """
    PRIMARY = 'Primary'
    POST = 'Post'
    DELIVERY = 'Delivery'
    HOLIDAY = 'Holiday'
    HOME = 'Home'
    VISITS = 'Visits'
    DEPARTMENT = 'Department'
    COMMUTERHOUSING = 'CommuterHousing'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AddressType from a JSON string"""
        return cls(json.loads(json_str))



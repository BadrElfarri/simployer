# coding: utf-8

"""
    HrConnect

    JWT token is required for authorization. Access to the API is granted through Simployer Admin Center: https://admincenter.simployer.com/    Endpoints with pagination support return following headers      x-has-next-page: True (indicates whether there are more records)      x-page: 1 (page numeration starts with 1)      x-page-size: 100 (records per page)      x-total-count: 120 (total number of records)      x-total-pages: 2 (total number of pages)

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from simployer_client.api.employees_api import EmployeesApi


class TestEmployeesApi(unittest.TestCase):
    """EmployeesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = EmployeesApi()

    def tearDown(self) -> None:
        pass

    def test_v1_employees_get(self) -> None:
        """Test case for v1_employees_get

        Retrieves employees with pagination.
        """
        pass


if __name__ == '__main__':
    unittest.main()

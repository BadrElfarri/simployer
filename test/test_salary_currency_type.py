# coding: utf-8

"""
    HrConnect

    JWT token is required for authorization. Access to the API is granted through Simployer Admin Center: https://admincenter.simployer.com/    Endpoints with pagination support return following headers      x-has-next-page: True (indicates whether there are more records)      x-page: 1 (page numeration starts with 1)      x-page-size: 100 (records per page)      x-total-count: 120 (total number of records)      x-total-pages: 2 (total number of pages)

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from simployer_client.models.salary_currency_type import SalaryCurrencyType

class TestSalaryCurrencyType(unittest.TestCase):
    """SalaryCurrencyType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSalaryCurrencyType(self):
        """Test SalaryCurrencyType"""
        # inst = SalaryCurrencyType()

if __name__ == '__main__':
    unittest.main()

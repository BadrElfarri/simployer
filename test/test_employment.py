# coding: utf-8

"""
    HrConnect

    JWT token is required for authorization. Access to the API is granted through Simployer Admin Center: https://admincenter.simployer.com/    Endpoints with pagination support return following headers      x-has-next-page: True (indicates whether there are more records)      x-page: 1 (page numeration starts with 1)      x-page-size: 100 (records per page)      x-total-count: 120 (total number of records)      x-total-pages: 2 (total number of pages)

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from simployer_client.models.employment import Employment

class TestEmployment(unittest.TestCase):
    """Employment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Employment:
        """Test Employment
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Employment`
        """
        model = Employment()
        if include_optional:
            return Employment(
                person_id = '',
                position_id = '',
                employment_id = '',
                employment_company_id = '',
                termination_cause_id = '',
                category_id = '',
                employee_id = '',
                employee_company_id = '',
                start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                employee_number = '',
                assignment_type = 'Percentage',
                assignment_value = 1.337,
                position_name = '',
                position_number = 56,
                code = 56,
                sub_code = 56,
                category_name = '',
                category_number = '',
                category_hour_unit = 'Undefined',
                category_hours_per_unit = 1.337
            )
        else:
            return Employment(
        )
        """

    def testEmployment(self):
        """Test Employment"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

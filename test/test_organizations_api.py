# coding: utf-8

"""
    HrConnect

    JWT token is required for authorization. Access to the API is granted through Simployer Admin Center: https://admincenter.simployer.com/    Endpoints with pagination support return following headers      x-has-next-page: True (indicates whether there are more records)      x-page: 1 (page numeration starts with 1)      x-page-size: 100 (records per page)      x-total-count: 120 (total number of records)      x-total-pages: 2 (total number of pages)

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from simployer_client.api.organizations_api import OrganizationsApi


class TestOrganizationsApi(unittest.TestCase):
    """OrganizationsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OrganizationsApi()

    def tearDown(self) -> None:
        pass

    def test_v1_organizations_get(self) -> None:
        """Test case for v1_organizations_get

        Retrieves organizations with pagination.
        """
        pass

    def test_v1_organizations_groups_affiliated_people_get(self) -> None:
        """Test case for v1_organizations_groups_affiliated_people_get

        Retrieves group-people relations with pagination.
        """
        pass

    def test_v1_organizations_groups_categories_get(self) -> None:
        """Test case for v1_organizations_groups_categories_get

        Retrieves group categories with pagination.
        """
        pass

    def test_v1_organizations_groups_categories_id_get(self) -> None:
        """Test case for v1_organizations_groups_categories_id_get

        Retrieves group category with given identifier.
        """
        pass

    def test_v1_organizations_groups_get(self) -> None:
        """Test case for v1_organizations_groups_get

        Retrieves groups with pagination.
        """
        pass

    def test_v1_organizations_groups_id_affiliated_people_get(self) -> None:
        """Test case for v1_organizations_groups_id_affiliated_people_get

        Retrieves group-people relation for given group.
        """
        pass

    def test_v1_organizations_groups_id_get(self) -> None:
        """Test case for v1_organizations_groups_id_get

        Retrieves a group with given identifier.
        """
        pass

    def test_v1_organizations_groups_person_id_get(self) -> None:
        """Test case for v1_organizations_groups_person_id_get

        Retrieves groups identifiers where given person affiliates.
        """
        pass

    def test_v1_organizations_hierarchy_get(self) -> None:
        """Test case for v1_organizations_hierarchy_get

        Retrieves organization hierarchy.
        """
        pass

    def test_v1_organizations_id_get(self) -> None:
        """Test case for v1_organizations_id_get

        Retrieves an organization with given identifier.
        """
        pass


if __name__ == '__main__':
    unittest.main()

from http import HTTPStatus

from rest_framework.test import APITestCase

import django
django.setup()

from model_mommy import mommy
from inmar_app.models import Location, Department, Category, SubCategory


class TestStoreView(APITestCase):
    base_path = '/api/v1/store'

    def setUp(self) -> None:
        self.location = mommy.make(Location, location='xyz')
        self.department = mommy.make(Department, department='aaa')
        self.category = mommy.make(Category, category='aa')
        self.subcategory = mommy.make(SubCategory, subcategory='a')

    def get_request_data(self):
        return {
            "data": {
                "sku": "UKR431",
                "location": self.location.id,
                "department": self.department.id,
                "category": self.category.id,
                "subcategory": self.subcategory.id
            }
        }

    def test_create_store_ok(self):
        """
        Test case to create store model
        """
        response = self.client.post(
            path=self.base_path, data=self.get_request_data()['data'])
        self.assertEqual(response.status_code, HTTPStatus.CREATED)

    def test_create_store_not_ok(self):
        """
        Test case for fail to create store model
        """
        response = self.client.post(
            path=self.base_path, data=self.get_request_data())
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)



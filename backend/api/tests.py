from django.test import TestCase
from django.test import Client
import json
from rest_framework import status


class APITest(TestCase):
    
    def setUp(self):
        self.invalid_payload = {
            'name': '',
            'age': 4,
            'breed': 'Pamerion',
            'color': 'White'
        }

    def test_valid_request(self):
        c = Client()
        with open('api/test/customers.txt') as fp:
            response = c.post(
                '/v1/api/customers_around/',
                {
                    'latitude': 53.339428,
                    'file': fp,
                    'longitude':-6.257664
                }
            )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_request(self):
        c = Client()
        response = c.post(
            '/v1/api/customers_around/',
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_invalid_file_request(self):
        c = Client(enforce_csrf_checks=True)
        with open('api/test/err.py') as fp:
            response = c.post(
                '/v1/api/customers_around/',
                {
                    'latitude': 53.339428,
                    'file': fp,
                    'longitude':-6.257664
                },
            )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_ascending_request(self):
        c = Client()
        with open('api/test/customers.txt') as fp:
            response = c.post(
                '/v1/api/customers_around/',
                {
                    'latitude': 53.339428,
                    'file': fp,
                    'longitude':-6.257664
                }
            )
            max_id = 0
            flag = True
            for i in response.json()['data']:
                if max_id<int(i['user_id']):
                    max_id = int(i['user_id'])
                else:
                    flag = False
                    break
        self.assertTrue(flag)

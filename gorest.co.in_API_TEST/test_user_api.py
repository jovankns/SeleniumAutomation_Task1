import requests
import unittest
from conftest import ValueStorage


class UserAPITests(unittest.TestCase):
    base_url = 'https://gorest.co.in/public/v2'
    access_token = 'dcc406f25ceee0155749d3f248a87019d8289371693f71f5d4196c3a1ecc6381'

    def test_1_create_new_user(self):
        endpoint = '/users'
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
        data = {
            'name': 'Jovan Kule',
            'email': 'jovankns@example.com',
            'gender': 'male',
            'status': 'active'
        }

        response = requests.post(self.base_url + endpoint, headers=headers, json=data)
        result = response.json()

        # Save the newly created user ID for future tests
        ValueStorage.existing_user_id: str = str(result['id'])

        self.assertEqual(response.status_code, 201)
        self.assertEqual(result['name'], 'Jovan Kule')
        self.assertEqual(result['email'], 'jovankns@example.com')

    def test_2_update_user_details(self):
        if ValueStorage.existing_user_id is None:
            self.fail("existing_user_id is not set")

        endpoint = f'/users/{ValueStorage.existing_user_id}'
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
        data = {
            'name': 'Updated Name',
            'email': 'updated_mail_2@example.com',
            'gender': 'male',
            'status': 'active'
        }

        response = requests.patch(self.base_url + endpoint, headers=headers, json=data)
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['name'], 'Updated Name')
        self.assertEqual(result['email'], 'updated_mail_2@example.com')

    def test_3_delete_user(self):
        if ValueStorage.existing_user_id is None:
            self.fail("existing_user_id is not set")

        endpoint = f'/users/{ValueStorage.existing_user_id}'
        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }

        response = requests.delete(self.base_url + endpoint, headers=headers)

        self.assertEqual(response.status_code, 204)


if __name__ == '__main__':
    unittest.main()

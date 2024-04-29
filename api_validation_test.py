import unittest
import requests

class TestAPIValidation(unittest.TestCase):
    def test_registration_api(self):
        # Define the registration data
        data = {'email': 'test@example.com', 'password': 'password', 'confirm-password': 'password'}

        # Make a POST request to the registration API endpoint
        response = requests.post('http://localhost:5000/submit_registration', data=data)

        # Check if the request was successful (status code 200)
        self.assertEqual(response.status_code, 200)

        # Check if the response contains the expected message
        self.assertIn('Registration successful!', response.text)

    # Add more test cases for other API endpoints as needed

if __name__ == '__main__':
    unittest.main()

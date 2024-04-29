import unittest
from flask import Flask
import sqlite3
from app import app

class TestIntegration(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

        # Create a test database
        self.conn = sqlite3.connect(':memory:')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE registrations
                          (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT, password TEXT)''')

    def tearDown(self):
        self.conn.close()

    def test_successful_registration(self):
        data = {'email': 'test@example.com', 'password': 'password', 'confirm-password': 'password'}
        response = self.app.post('/submit_registration', data=data, follow_redirects=True)
        self.assertIn(b'Registration successful!', response.data)

        # Check if data is inserted into the database
        self.c.execute("SELECT * FROM registrations WHERE email=?", ('test@example.com',))
        result = self.c.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[1], 'test@example.com')  # Check email
        self.assertEqual(result[2], 'password')  # Check password

    def test_password_mismatch_registration(self):
        data = {'email': 'test@example.com', 'password': 'password', 'confirm-password': 'wrongpassword'}
        response = self.app.post('/submit_registration', data=data)
        self.assertIn(b'Passwords do not match!', response.data)

if __name__ == '__main__':
    unittest.main()

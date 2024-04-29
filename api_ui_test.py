import requests

# Define base URL for API requests
BASE_URL = 'http://127.0.0.1:5000/'

# Function to submit registration form
def submit_registration(email, password, confirm_password):
    url = BASE_URL + 'submit_registration'
    data = {
        'email': email,
        'password': password,
        'confirm-password': confirm_password
    }
    response = requests.post(url, data=data)
    return response.text

# Test registration submission
def test_registration():
    email = 'test@example.com'
    password = 'password123'
    confirm_password = 'password123'
    response = submit_registration(email, password, confirm_password)
    print(response)

if __name__ == '__main__':
    test_registration()

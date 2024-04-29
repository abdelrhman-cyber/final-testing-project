from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(5, 9)  # wait time between requests

    @task
    def register(self):
        # Define the payload with test data
        payload = {
            "email": "test@example.com",
            "password": "password123",
            "confirm-password": "password123"
        }
        
        # Send a POST request to the registration page
        response = self.client.post("/submit_registration", data=payload)
        
        # Check if the registration was successful
        if response.status_code == 200:
            print("Registration successful")
        else:
            print("Registration failed")

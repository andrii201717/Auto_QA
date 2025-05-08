import requests


class TestEmployeeApi:
    base_url = "http://5.101.50.27:8000"
    client_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJoYXJyeXBvdHRlciIsInJvbGUiOiJhZG1pbiIsImV4cCI6MTc0NjQ1ODkxM30.Elw9ExSKMizCP4TJM-DWqzJeSQ7jymkBZuhG_DI7OQs"

    def test_user_create(self):
        data_json = {
            "first_name": "Andrii",
            "last_name": "Tabaka",
            "company_id": 317,
            "email": "andrii@mail.com",
            "phone": "+49123456789",
            "birthdate": "1990-06-17",
            "is_active": True
        }

        response = requests.post(f"{self.base_url}/employee/create/", json=data_json)
        assert response.status_code == 200

    def test_user_info(self):
        user_id = 9

        response = requests.get(f"{self.base_url}/employee/info/{user_id}")
        assert response.status_code == 200

    def test_user_update(self):
        data_json = {
            "company_id": 320,
            "email": "user@32.com",
            "phone": "+49012345678",
        }

        response = requests.patch(f"{self.base_url}/employee/change/1/?client_token={self.client_token}", json=data_json)
        assert response.status_code == 200
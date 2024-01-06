from lib.assertions import Assertions
from lib.base_case import BaseCase
from lib.custom_requests import CustomRequests


class TestUserRegister(BaseCase):
    def test_create_user_successfully(self):
        data = self.prepare_registration_data()
        resp = CustomRequests.post("/user", data=data)
        Assertions.assert_correct_response_status(resp, 200)
        Assertions.assert_json_has_key(resp, "id")

    def test_create_user_with_existing_email(self):
        email = "vinkotov@example.com"
        data = self.prepare_registration_data(email)
        resp = CustomRequests.post("/user", data=data)
        resp_content = resp.content.decode("utf-8")
        assert resp.status_code == 400, f"Unexpected status code {resp.status_code}"
        assert resp_content == f"Users with email '{email}' already exists", f"Unexpected response content: {resp_content}"


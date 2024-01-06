from my_tests.api.lib.assertions import Assertions
from my_tests.api.lib.base_case import BaseCase
from my_tests.api.lib.custom_requests import CustomRequests


class TestUserGet(BaseCase):
    def setup(self):
        self.email = "vinkotov@example.com"

    def test_get_user_details_not_auth(self):
        response = CustomRequests.get("/user/1")
        Assertions.assert_json_has_key(response, "username")
        Assertions.assert_json_has_not_key(response, "email")
        Assertions.assert_json_has_not_key(response, "firstName")
        Assertions.assert_json_has_not_key(response, "lastName")

    def test_get_user_details_auth_as_same_user(self):
        data = {
            'email': self.email,
            'password': "1234",
        }

        resp1 = CustomRequests.post("/user/login", data=data)
        auth_sid = self.get_cookie(resp1, "auth_sid")
        token = self.get_header(resp1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(resp1, "user_id")
        resp2 = CustomRequests.get(
            f"/user/{user_id_from_auth_method}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},)

        expected_keys = ["username", "email", "firstName", "lastName"]
        Assertions.assert_json_has_keys(resp2, expected_keys)

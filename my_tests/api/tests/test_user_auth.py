import pytest
from my_tests.api.lib.custom_requests import CustomRequests


class TestUserAuth:
    negative_check_params = ["no_cookie", "no_token"]

    def setup(self):
        data = {
            'email': "vinkotov@example.com",
            'password': "1234",
        }
        response1 = CustomRequests.get("/api/user/login", data=data)
        assert "auth_sid" in response1.cookies, "There is no auth cookie in the incoming response"
        assert "x-csrf-token" in response1.headers, "There is no CSRF token header in the incoming response"
        assert "user_id" in response1.json(), "There is no user id in the incoming response"

        self.auth_sid = response1.cookies.get("auth_sid")
        self.token = response1.headers.get("x-csrf-token")
        self.user_id_from_auth_method = response1.json().get("user_id")

    def test_auth_self(self):
        response2 = CustomRequests.get("/api/user/auth", headers={"x-csrf-token": self.token}, cookies={"auth_sid": self.auth_sid})
        assert "user_id" in response2.json(), "There is no user id in the second response"
        user_id_from_check_method = response2.json().get("user_id")
        assert self.user_id_from_auth_method == user_id_from_check_method, "User id from auth method is not equal to user " \
                                                                      "id from check method"

    @pytest.mark.parametrize('condition', negative_check_params)
    def test_negative_auth_check(self, condition):
        if condition == "no_cookie":
            resp2 = CustomRequests.get("/api/user/auth", headers={'x-csrf-token': self.token})
        else:
            resp2 = CustomRequests.get("/api/user/auth", cookies={'auth_sid': self.auth_sid})

        assert "user_id" in resp2.json(), "There is no user_id in the second response"
        user_id_from_check_method = resp2.json()["user_id"]
        assert user_id_from_check_method == 0, f"User authorized with condition {condition}"








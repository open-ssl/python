from lib.custom_requests import CustomRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserEdit(BaseCase):
    def test_edit_just_created_user(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        resp1 = CustomRequests.post("/user", data=register_data)
        Assertions.assert_correct_response_status(resp1, 200)
        Assertions.assert_json_has_key(resp1, "id")

        email = register_data.get("email")
        first_name = register_data.get("firstName")
        password = register_data.get("password")
        user_id = self.get_json_value(resp1, "id")

        # LOGIN
        login_data = {
            "email": email,
            "password": password,
        }
        resp2 = CustomRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(resp2, "auth_sid")
        token = self.get_header(resp2, "x-csrf-token")

        # EDIT
        new_name = "Changed_name"
        resp3 = CustomRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name},
        )

        Assertions.assert_correct_response_status(resp3, 200)

        # GET
        resp4 = CustomRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
        )
        Assertions.assert_json_value_by_name(resp4, "firstName", new_name, "Wrong name of the user after edit")

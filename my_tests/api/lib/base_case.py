import json
import requests
from datetime import datetime


class BaseCase:
    """
    Default custom logic for base test starting
    """

    def get_cookie(self, response: requests.Response, cookie_name):
        """
        Get cookie value from Response by name
        """
        return response.cookies.get(cookie_name)

    def get_header(self, response: requests.Response, header_name):
        """
        Get header value from Response by name
        """
        return response.headers.get(header_name)

    def get_json_value(self, response: requests.Response, json_key):
        """
        Get value from Response json body by name
        """
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert json_key in response_as_dict, f"Response JSON doesn't have key with name {json_key}"
        return response_as_dict.get(json_key)

    @staticmethod
    def prepare_registration_data(email=None):
        if email is None:
            base_part = "learnqa"
            domain = "example.com"
            random_part = datetime.now().strftime("%m%d%Y%H%M%S")
            email = f"{base_part}{random_part}@{domain}"

        return {
            "password": "123",
            "username": "learnqa",
            "firstName": "learnqa",
            "lastName": "learnqa",
            "email": email,
        }


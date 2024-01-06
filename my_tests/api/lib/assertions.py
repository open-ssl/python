from requests import Response
import json


class Assertions:
    """
    Default custom logic for test assertions
    """
    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        """
        Check has some key and one's value in incoming Response
        If not assert a given error
        """
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesn't have key {name}"
        assert response_as_dict.get(name) == expected_value, error_message

    @staticmethod
    def assert_json_has_key(response: Response, name: str):
        """
        Check has some key in incoming Response?
        """
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesn't have key {name}"

    @staticmethod
    def assert_json_has_not_key(response: Response, name: str):
        """
        Check has no some key in incoming Response?
        """
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert name not in response_as_dict, f"Response JSON mustn't have key {name}. But it is present."

    @staticmethod
    def assert_json_has_keys(response: Response, key_names: list[str]):
        """
        Check that incoming Response has many particular keys?
        """
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        for name in key_names:
            assert name in response_as_dict, f"Response JSON doesn't have key {name}"

    @staticmethod
    def assert_correct_response_status(response: Response, expected_status: int):
        """
        Check HTTP-status of incoming Response
        """
        assert response.status_code == expected_status, f"Unexpected status code! Actual: {response.status_code}, " \
                                                        f"Expected: {expected_status}"





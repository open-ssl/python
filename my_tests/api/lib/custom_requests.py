import requests
from my_tests.api.lib.logger import Logger
from my_tests.api.environment import ENV_OBJECT


class CustomRequests:
    @staticmethod
    def get(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return CustomRequests._send(url, data, headers, cookies, method="GET")

    @staticmethod
    def post(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return CustomRequests._send(url, data, headers, cookies, method="POST")

    @staticmethod
    def put(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return CustomRequests._send(url, data, headers, cookies, method="PUT")

    @staticmethod
    def delete(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return CustomRequests._send(url, data, headers, cookies, method="DELETE")

    @staticmethod
    def _send(url: str, data: dict, headers: dict, cookies: dict, method: str):
        url = f"{ENV_OBJECT.get_base_url()}{url}"

        if headers is None:
            headers = {}

        if cookies is None:
            cookies = {}

        Logger.add_request(url, data, headers, cookies, method)

        if method == "GET":
            response = requests.get(url, params=data, headers=headers, cookies=cookies)
        elif method == "POST":
            response = requests.post(url, data=data, headers=headers, cookies=cookies)
        elif method == "PUT":
            response = requests.put(url, data=data, headers=headers, cookies=cookies)
        elif method == "DELETE":
            response = requests.delete(url, data=data, headers=headers, cookies=cookies)
        else:
            raise Exception(f"Unsupported HTTP method: '{method}' for request")

        Logger.add_response(response)

        return response

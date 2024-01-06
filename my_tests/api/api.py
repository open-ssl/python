import requests


def main():
    payload = {
        "login": "secret_login",
        "password": "secret_pass",
    }
    resp1 = requests.post("", data=payload)
    cookie_value = resp1.cookies.get("auth_cookie")
    cookies = {}
    if cookie_value is not None:
        cookies.update({"auth_cookie": cookie_value})

    resp2 = requests.post("", cookies=cookies)
    print(resp2.text)
    print(resp2.status_code)


if __name__ == '__main__':
    main()

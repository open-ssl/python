from lib.custom_requests import CustomRequests


class TestSomeApi:
    def test_hello_call(self):
        name = "Stanislav"
        data = {'name': name}
        response = CustomRequests.get("/hello", data=data)
        assert response.status_code == 200, "Wrong test response code {}".format(response.status_code)

        resp_dict = response.json()
        assert "answer" in resp_dict, "There is no field 'answer' in the incoming response"
        expected_response_text = f'Hello, {name}'
        actual_text = resp_dict.get("answer")
        assert expected_response_text == actual_text

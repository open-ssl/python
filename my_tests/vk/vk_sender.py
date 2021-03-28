import requests

AGAIN_COMMAND = 'again'
LEN_MESSAGE = 140


class VKSender:
    ACCEPT_CODE = 200
    RESPONSE_GET_REQUEST = 'response'
    ERROR_GET_REQUEST = 'error'
    POST_ID_GET_REQUEST = 'post_id'

    def __init__(self, user_id, user_token):
        self.user_info = requests.get(f"https://api.vk.com/method/users.get?\
            user_id={user_id}&v=5.52&access_token={user_token}")
        self.has_connect = self.user_info.status_code == self.ACCEPT_CODE

        if not self.has_connect:
            self.greeting_message = 'Sorry I can\'t get data from VK server.\n\
            Please check authorisation data and internet connection'
            return

        self.user_info = self.user_info.json()[self.RESPONSE_GET_REQUEST][0]
        self.user_name = self.user_info['first_name']
        self.send_message_request_text = \
        f'https://api.vk.com/method/wall.post?owner_id={user_id}&v=5.52\
        &access_token={user_token}&message='
        self.greeting_message = f"Hello, {self.user_name}! \n\
        Let's send message!"

    def send_message(self):
        while True:
            user_message = input(
                'Type your message with length not more 140 symbols:\n'
            )
            if len(user_message) > LEN_MESSAGE:
                print('Len of your message is more than 140')
                continue
            # otherwise second and more sending will concat
            # with request that have contain previous message
            send_message_request_text = self.send_message_request_text
            send_message_request_text += user_message
            message_request_answer = requests.get(
                send_message_request_text
            ).json()
            if self.ERROR_GET_REQUEST in message_request_answer:
                return 'Check rights wall posting for your token'
            print('Your message: {0} was posted with id {1}'.format(
                user_message,
                message_request_answer[self.RESPONSE_GET_REQUEST]
                                      [self.POST_ID_GET_REQUEST]
            ))
            break


# my vk id is '72612637'
if __name__ == '__main__':
    print("Hey, This is vk_sender!')'")
    while True:
        user_id = input('Type your VK user id\n')
        user_token = input('Type your VK token\n')
        vk_sender = VKSender(user_id, user_token)

        print(vk_sender.greeting_message)
        if not vk_sender.has_connect:
            print('Please try again')
            continue
        exit = 1
        counter = 0
        while exit:
            vk_sender.send_message()
            exit = input(f"If you want send another one message type \
                '{AGAIN_COMMAND}'.\nFor exit type 'exit'\
                 or whatever you want =)\n")
            exit = [0, 1][exit == AGAIN_COMMAND]
            counter += 1

        print(f'You sent {counter} messages using this sender.')
        break

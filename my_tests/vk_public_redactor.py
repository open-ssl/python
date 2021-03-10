import requests
from time import sleep

AGAIN_COMMAND = 'again'
LEN_MESSAGE = 140
TOKEN = ''
# link = 
# для получения токена 
# https://oauth.vk.com/authorize?client_id=group_id&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends,groups&response_type=token&v=5.52

class VKSender:
    ACCEPT_CODE = 200
    RESPONSE_GET_REQUEST = 'response'
    ERROR_GET_REQUEST = 'error'
    POST_ID_GET_REQUEST = 'post_id'
    ours_ids = [
        # user ids
        # 65851797,
        # 69147860,
        # 75551977,
        # 94733741,
        # 103980445,
        # 107224165,
        # 132996659,
        # 138130127,
        # 139745151,
        # 144369565,
        # 148267583,
        # 191012078,
        # 197538148,
        # 215970484,
        # 243311812,
        # 284130732,
        # 174498280,
        # 296457938,
        # 147979131,
        # 298416192,
        # 524869113,
        # 133185031,
        # 514610444,
        # 142729204,
        # 235489974,
        # 224006252,
        # 255045509
    ]

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

        self.users_list = requests.get(
        f'https://api.vk.com/method/groups.getMembers?user_id={user_id}&v=5.52&access_token={user_token}&group_id={54414941}&v=5.52'
        ).json()
        # Let's send message!"


    def delete_user_from_group(self, user_ids_list):
        
        for _id in user_ids_list:
            sleep(0.05)
            if _id not in self.ours_ids:
                # удалим
                tmp = requests.get(
                    f'https://api.vk.com/method/groups.removeUser?user_id={_id}&v=5.52&access_token={user_token}&group_id={54414941}&v=5.52'
                ).json() 
                print(tmp)
                continue
            print('наш ид')

        print('ok')



    # def send_message(self):
    #     while True:
    #         user_message = input(
    #             'Type your message with length not more 140 symbols:\n'
    #         )
    #         if len(user_message) > LEN_MESSAGE:
    #             print('Len of your message is more than 140')
    #             continue
    #         # otherwise second and more sending will concat
    #         # with request that have contain previous message
    #         send_message_request_text = self.send_message_request_text
    #         send_message_request_text += user_message
    #         message_request_answer = requests.get(
    #             send_message_request_text
    #         ).json()
    #         if self.ERROR_GET_REQUEST in message_request_answer:
    #             return 'Check rights wall posting for your token'
    #         print('Your message: {0} was posted with id {1}'.format(
    #             user_message,
    #             message_request_answer[self.RESPONSE_GET_REQUEST]
    #                                   [self.POST_ID_GET_REQUEST]
    #         ))
    #         break


# my vk id is '72612637'
if __name__ == '__main__':
    print("Hey, This is vk_sender!')'")
    user_id = 72612637
    user_token = TOKEN
    vk_sender = VKSender(user_id, user_token)

    print(vk_sender.user_info)
    print()
    user_dict = vk_sender.users_list['response']
    user_list = user_dict['items']
    print(len(user_list))
    vk_sender.delete_user_from_group(user_list)
    
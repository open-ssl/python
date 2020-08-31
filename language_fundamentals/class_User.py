'''
Create a class named User and create a way to check the number of users
(number of instances) were created,
so that the value can be accessed as a class attribute.
'''


class User():

    user_count = 0

    def __init__(self, username):
        User.user_count += 1
        self.username = username


# u1 = User("johnsmith10")
# print(u1.username)
# print(u1.user_count)
#
# u2 = User("marysue1989")
# print(User.user_count)
#
# u3 = User("milan_rodrick")
# print(User.user_count)

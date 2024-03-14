class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0


user_1 = User("001", "Angela")
user_2 = User("002", "Jack")
user_1.followers = 7
print(user_1.followers)
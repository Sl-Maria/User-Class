class User():
    def __init__(self, id, name):
        self._id = id
        self._name = name
        self._access_level = 'user'

class Admin(User):
    def __init__(self, id, name):
        super().__init__(id, name)
        self._access_level = 'admin'
        self.__user_list = []
    def add_user(self, user):
        self.__user_list.append(user)

    def remove_user(self, user):
        self.__user_list.remove(user)

    def get_user_list(self):
        return self.__user_list

admin1 = Admin('001', 'Bob')
user1 = User('002', 'Alice')
user2 = User('003', 'Eve')
user3 = User('004', 'Sue')

admin1.add_user(user1)
admin1.add_user(user2)
admin1.add_user(user3)

for user in admin1.get_user_list():
    print(user._id,user._name)

admin1.remove_user(user2)

for user in admin1.get_user_list():
    print(user._id,user._name)
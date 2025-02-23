from models.user_dao import UserDAO

class UserController:
    def __init__(self):
        self.user_dao = UserDAO()

    def register_user(self, username, password, role):
        self.user_dao.register_user(username, password, role)

    def login_user(self, username, password):
        return self.user_dao.login_user(username, password)

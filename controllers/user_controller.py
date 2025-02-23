from models.user_dao import UserDAO

class UserController:
    def __init__(self):
        self.user_dao = UserDAO()

    def register_user(self, username, password, role):
        if not username or not password or not role:
            print("Error: All fields are required!")
            return

        role = role.strip().lower().replace(" ", "")
        if role not in ["admin", "jobseeker"]:
            print("Error: Invalid role! Choose 'Admin' or 'Job Seeker'.")
            return

        self.user_dao.register_user(username, password, role)
        print("User registered successfully!")

    def login_user(self, username, password):
        if not username or not password:
            print("Error: Username and password are required!")
            return None

        return self.user_dao.login_user(username, password)

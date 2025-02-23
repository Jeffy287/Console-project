from models.user_dao import UserDAO

class UserController:
    @staticmethod
    def register_user(username, password, role):
        if role.lower() == "job seeker":
            role = "Job Seeker"
        UserDAO.create_user(username, password, role)

    @staticmethod
    def login_user(username, password):
        user = UserDAO.get_user_by_username(username)
        if user and user[2] == password:
            return user
        return None

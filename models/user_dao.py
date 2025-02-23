from models.database import create_connection

class UserDAO:
    @staticmethod
    def create_user(username, password, role):
        connection = create_connection()
        cursor = connection.cursor()
        query = "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)"
        cursor.execute(query, (username, password, role))
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def get_user_by_username(username):
        connection = create_connection()
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        return result

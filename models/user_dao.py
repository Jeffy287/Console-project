from models.database import get_db_connection

class UserDAO:
    def register_user(self, username, password, role):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)", (username, password, role))
        conn.commit()
        cursor.close()
        conn.close()

    def login_user(self, username, password):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, role FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        return user

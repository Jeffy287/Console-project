from models.database import create_connection

class JobDAO:
    @staticmethod
    def create_job(title, description, posted_by):
        connection = create_connection()
        cursor = connection.cursor()
        query = "INSERT INTO jobs (title, description, posted_by) VALUES (%s, %s, %s)"
        cursor.execute(query, (title, description, posted_by))
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def get_all_jobs():
        connection = create_connection()
        cursor = connection.cursor()
        query = "SELECT * FROM jobs"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result

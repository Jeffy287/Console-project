from models.database import create_connection

class ApplicationDAO:
    @staticmethod
    def apply_for_job(user_id, job_id):
        connection = create_connection()
        cursor = connection.cursor()
        query = "INSERT INTO applications (user_id, job_id) VALUES (%s, %s)"
        cursor.execute(query, (user_id, job_id))
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def get_application_status(user_id, job_id):
        connection = create_connection()
        cursor = connection.cursor()
        query = "SELECT status FROM applications WHERE user_id = %s AND job_id = %s"
        cursor.execute(query, (user_id, job_id))
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        return result[0] if result else None

    @staticmethod
    def update_application_status(application_id, status):
        connection = create_connection()
        cursor = connection.cursor()
        query = "UPDATE applications SET status = %s WHERE application_id = %s"
        cursor.execute(query, (status, application_id))
        connection.commit()
        cursor.close()
        connection.close()

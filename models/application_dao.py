from models.database import get_db_connection

class ApplicationDAO:
    def apply_for_job(self, user_id, job_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO applications (user_id, job_id) VALUES (%s, %s)", (user_id, job_id))
        conn.commit()
        cursor.close()
        conn.close()

    def check_application_status(self, user_id, job_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT status FROM applications WHERE user_id = %s AND job_id = %s", (user_id, job_id))
        status = cursor.fetchone()
        cursor.close()
        conn.close()
        return status

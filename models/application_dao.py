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
        return status[0] if status else "No Application Found"

    def view_all_applications(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT applications.id, users.username, jobs.title, applications.status 
            FROM applications 
            JOIN users ON applications.user_id = users.id 
            JOIN jobs ON applications.job_id = jobs.id
        """)
        applications = cursor.fetchall()
        cursor.close()
        conn.close()
        return applications

    def update_application_status(self, application_id, new_status):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE applications SET status = %s WHERE id = %s", (new_status, application_id))
        conn.commit()
        cursor.close()
        conn.close()

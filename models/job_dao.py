from models.database import get_db_connection

class JobDAO:
    def create_job(self, title, description):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO jobs (title, description) VALUES (%s, %s)", (title, description))
        conn.commit()
        cursor.close()
        conn.close()

    def list_jobs(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM jobs")
        jobs = cursor.fetchall()
        cursor.close()
        conn.close()
        return jobs

from models.job_dao import JobDAO

class JobController:
    def __init__(self):
        self.job_dao = JobDAO()

    def create_job(self, title, description):
        self.job_dao.create_job(title, description)

    def view_jobs(self):
        return self.job_dao.view_jobs()

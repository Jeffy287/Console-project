from models.application_dao import ApplicationDAO

class ApplicationController:
    def __init__(self):
        self.application_dao = ApplicationDAO()

    def apply_for_job(self, user_id, job_id):
        self.application_dao.apply_for_job(user_id, job_id)

    def check_application_status(self, user_id, job_id):
        return self.application_dao.check_application_status(user_id, job_id)

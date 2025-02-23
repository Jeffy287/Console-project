from models.application_dao import ApplicationDAO

class ApplicationController:
    @staticmethod
    def apply_for_job(user_id, job_id):
        ApplicationDAO.apply_for_job(user_id, job_id)

    @staticmethod
    def check_application_status(user_id, job_id):
        return ApplicationDAO.get_application_status(user_id, job_id)

    @staticmethod
    def update_application_status(application_id, status):
        ApplicationDAO.update_application_status(application_id, status)

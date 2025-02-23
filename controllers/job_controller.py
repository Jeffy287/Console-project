from models.job_dao import JobDAO

class JobController:
    @staticmethod
    def post_job(title, description, posted_by):
        JobDAO.create_job(title, description, posted_by)

    @staticmethod
    def list_jobs():
        return JobDAO.get_all_jobs()

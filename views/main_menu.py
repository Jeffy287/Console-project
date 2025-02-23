from controllers.user_controller import UserController
from controllers.job_controller import JobController
from controllers.application_controller import ApplicationController

user_controller = UserController()
job_controller = JobController()
application_controller = ApplicationController()

def main():
    while True:
        print("\n===== Job Recruitment System =====")
        print("1. Register")
        print("2. Login")
        print("3. View Jobs")
        print("4. Apply for Job")
        print("5. Check Application Status")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            role = input("Enter role (admin/jobSeeker): ")
            user_controller.register_user(username, password, role)
            print("Registered successfully!")

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = user_controller.login_user(username, password)

            if user:
                user_id, role = user
                if role == "admin":
                    while True:
                        print("\n===== Admin Panel =====")
                        print("1. Create Job Posting")
                        print("2. View Job Applications")
                        print("3. Logout")
                        admin_choice = input("Enter your choice: ")

                        if admin_choice == "1":
                            title = input("Enter job title: ")
                            description = input("Enter job description: ")
                            job_controller.create_job(title, description)
                            print("Job posted successfully!")

                        elif admin_choice == "2":
                            applications = application_controller.view_all_applications()
                            for app in applications:
                                print(f"Application ID: {app[0]}, User: {app[1]}, Job: {app[2]}, Status: {app[3]}")
                            app_id = input("Enter Application ID to approve/reject: ")
                            new_status = input("Enter status (Accepted/Rejected): ")
                            application_controller.update_application_status(app_id, new_status)
                            print("Application status updated!")

                        elif admin_choice == "3":
                            break

                elif role == "jobSeeker":
                    while True:
                        print("\n===== Job Seeker Panel =====")
                        print("1. View Jobs")
                        print("2. Apply for Job")
                        print("3. Check Application Status")
                        print("4. Logout")
                        js_choice = input("Enter your choice: ")

                        if js_choice == "1":
                            jobs = job_controller.view_jobs()
                            for job in jobs:
                                print(f"Job ID: {job[0]}, Title: {job[1]}, Description: {job[2]}")

                        elif js_choice == "2":
                            job_id = input("Enter Job ID: ")
                            application_controller.apply_for_job(user_id, job_id)
                            print("Applied successfully!")

                        elif js_choice == "3":
                            job_id = input("Enter Job ID: ")
                            print(application_controller.check_application_status(user_id, job_id))

                        elif js_choice == "4":
                            break

main()

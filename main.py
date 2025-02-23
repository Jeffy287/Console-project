from views.main_menu import MainMenu
from controllers.user_controller import UserController
from controllers.job_controller import JobController
from controllers.application_controller import ApplicationController

def main():
    menu = MainMenu()
    user_controller = UserController()
    job_controller = JobController()
    application_controller = ApplicationController()

    logged_in_user = None  # Keep track of logged-in user
    role = None  # Store user role (admin/job seeker)

    while True:
        # Show the appropriate menu based on role
        if logged_in_user:
            menu.show_menu(role)
        else:
            menu.show_menu()

        choice = menu.get_choice()

        if choice == '1':  # Admin: Create Job Posting, or Job Seeker: Register
            if logged_in_user and role == "admin":
                job_title = input("Enter job title: ")
                job_description = input("Enter job description: ")
                job_controller.create_job(job_title, job_description)
                print("Job posted successfully!")
            else:
                username = input("Enter username: ")
                password = input("Enter password: ")
                role = input("Enter role (Job Seeker or Admin): ").lower()
                user_controller.register_user(username, password, role)

        elif choice == '2':  # Login (for both Admin and Job Seeker)
            if logged_in_user:
                logged_in_user = None
                role = None
                print("Logged out successfully!")
            else:
                username = input("Enter username: ")
                password = input("Enter password: ")
                user = user_controller.login_user(username, password)
                if user:
                    logged_in_user = user
                    role = user[3]  # Assuming role is stored in index 3 (jobSeeker or admin)
                    print(f"Welcome {role.capitalize()}!")
                else:
                    print("Invalid username or password.")

        elif choice == '3':  # View jobs
            jobs = job_controller.list_jobs()
            if jobs:
                for job in jobs:
                    print(f"Job ID: {job[0]}, Title: {job[1]}, Description: {job[2]}")
            else:
                print("No jobs available.")

        elif choice == '4':  # Apply for a job (Job Seeker only)
            if role == "job seeker":
                username = input("Enter username: ")
                password = input("Enter password: ")
                user = user_controller.login_user(username, password)
                if user:
                    job_id = int(input("Enter job ID to apply for: "))
                    application_controller.apply_for_job(user[0], job_id)
                    print("You have applied for the job!")
                else:
                    print("Invalid username or password.")

        elif choice == '5':  # Check application status
            if role == "job seeker":
                username = input("Enter username: ")
                password = input("Enter password: ")
                user = user_controller.login_user(username, password)
                if user:
                    job_id = int(input("Enter job ID: "))
                    status = application_controller.check_application_status(user[0], job_id)
                    print(f"Your application status: {status}")
                else:
                    print("Invalid username or password.")

        elif choice == '6':  # Exit the system
            print("Exiting the system.")
            break

if __name__ == "__main__":
    main()

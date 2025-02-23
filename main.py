from views.main_menu import MainMenu
from controllers.user_controller import UserController
from controllers.job_controller import JobController
from controllers.application_controller import ApplicationController

def main():
    menu = MainMenu()  # Display menu to user
    user_controller = UserController()  # Handles user registration/login
    job_controller = JobController()  # Handles job posting and listing
    application_controller = ApplicationController()  # Handles job applications

    while True:
        menu.show_menu()  # Display menu
        choice = menu.get_choice()  # Get user input for choice

        if choice == '1':  # Register user
            username = input("Enter username: ")
            password = input("Enter password: ")
            role = input("Enter role (Job Seeker): ")
            user_controller.register_user(username, password, role)

        elif choice == '2':  # Login user
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = user_controller.login_user(username, password)
            if user:
                print(f"Welcome {user[1]}!")
            else:
                print("Invalid username or password.")

        elif choice == '3':  # View available jobs
            jobs = job_controller.list_jobs()  # Fetch list of jobs
            if jobs:
                for job in jobs:
                    print(f"Job ID: {job[0]}, Title: {job[1]}, Description: {job[2]}")
            else:
                print("No jobs available.")

        elif choice == '4':  # Apply for a job
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

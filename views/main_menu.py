class MainMenu:
    def show_menu(self, role=None):
        print("\n===== Job Recruitment System =====")
        if role == "admin":
            print("1. Create Job Posting")
            print("2. View Job Applications")
            print("3. View Jobs")
            print("4. Logout")
        else:
            print("1. Register")
            print("2. Login")
            print("3. View Jobs")
            print("4. Apply for Job")
            print("5. Check Application Status")
            print("6. Exit")

    def get_choice(self):
        choice = input("Enter your choice: ")
        return choice

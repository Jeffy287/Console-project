class MainMenu:
    def show_menu(self):
        print("\n===== Job Recruitment System =====")
        print("1. Register")
        print("2. Login")
        print("3. View Jobs")
        print("4. Apply for Job")
        print("5. Check Application Status")
        print("6. Exit")

    def get_choice(self):
        choice = input("Enter your choice: ")
        return choice

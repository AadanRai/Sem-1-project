from analytics import run_analytics_dashboard

class User:
    def __init__(self, username, fullname, role):
        self.username = username
        self.fullname = fullname
        self.role = role

    def view_profile(self):
        print(f"\n--- Profile ---")
        print(f"Username: {self.username}")
        print(f"Name: {self.fullname}")
        print(f"Role: {self.role}")

class Admin(User):
    def __init__(self, username, fullname):
        super().__init__(username, fullname, "admin")

    def admin_menu(self):
        while True:
            print("\n== Admin Menu ==")
            print("1. Add Student")
            print("2. Update Student")
            print("3. Delete Student")
            print("4. View Student")
            print("5. Generate Reports")
            print("0. Logout")
            choice = input("Enter choice: ")

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.update_student()
            elif choice == "3":
                self.delete_student()            
            elif choice == "4":
                self.view_student()
            elif choice == "5":
                run_analytics_dashboard()
            elif choice == "0":
                print("Logging out...")
                break
            else:
                print("Invalid choice. Try again.")

    def add_student(self):
        print("\n== Add New Student ==")
        username = input("Enter username: ")
        fullname = input("Enter full name: ")
        age = input("Enter age: ")
        role = "student"
        # Check if username already exists
        with open("users.txt", "r") as f:
            for line in f:
                if line.startswith(username + ","):
                    print("❌ Username already exists!")
                    return
        # Append new student data to users.txt
        with open("users.txt", "a") as f:
            f.write(f"{username},{fullname},{role}\n")

    # Add grades entry for the student (initialize with zeros)
        with open("grades.txt", "a") as f:
            f.write(f"{username}:0,0,0,0,0\n")

    # Add ECA entry for the student (initialize empty)
        with open("eca.txt", "a") as f:
            f.write(f"{username}:\n")

        print(f"✅ New student {fullname} added with username '{username}'!")

#         add_student() method prompts for:

# username, fullname, and age (ID is auto-generated).

# Appends new student data into users.txt.

# Initializes an entry in grades.txt (with all zeros for grades) and eca.txt (empty list of activities).

    def view_student(self):
        import os
        print("\n== View Student Profile ==")
        username = input("Enter student username: ")

        # Find student from users.txt
        with open("users.txt", "r") as f:
            students = f.readlines()

         # 1. Load user info
        found = False
        try:
            with open("users.txt", "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) == 3:
                        u, fullname, role = parts
                        if u == username and role == "student":
                            print("\n📄 Student Profile:")
                            print(f"🆔 ID: {u}")
                            print(f"👤 Name: {fullname}")
                            print(f"🎓 Role: {role}")
                            found = True
                            break
            if not found:
                print("❌ Student not found.")
                return
        except FileNotFoundError:
            print("❌ users.txt not found.")
            return
                
 # 2. Load grades
        try:
            with open("grades.txt", "r") as f:
                for line in f:
                    u, grade_data = line.strip().split(":")
                    if u == username:
                        grades = grade_data.split(",")
                        print("\n📘 Grades:")
                        for i, grade in enumerate(grades, 1):
                            print(f"  Subject {i}: {grade}")
                        break
        except FileNotFoundError:
            print("⚠️ grades.txt not found.")
    
    # 3. Load ECA
        try:
            with open("eca.txt", "r") as f:
                for line in f:
                    u, eca_data = line.strip().split(":")
                    if u == username:
                        ecas = eca_data.split(",") if eca_data.strip() else []
                        print("\n🎯 ECA Activities:")
                        if ecas:
                            for activity in ecas:
                                print(f"  - {activity}")
                        else:
                            print("  None")
                        break
        except FileNotFoundError:
            print("⚠️ eca.txt not found.")
            #             view_student() method allows the admin to input a student ID.

# It searches users.txt for the student based on the ID.

# If found, it:

# Displays the student’s basic details (name, role).

# Pulls grades from grades.txt and shows them.

# Displays ECA activities from eca.txt.

# If no student is found, it shows an error message.


    def update_student(self):
        print("\n== Update Student ==")
        username = input("Enter student username to update: ")

    # Check if student exists
        exists = False
        with open("users.txt", "r") as f:
            users = f.readlines()

        for line in users:
            u, name, role = line.strip().split(",")
            if u == username and role == "student":
                exists = True
                break

        if not exists:
            print("❌ Student not found.")
            return

    # Show update options
        print("\nWhat would you like to update?")
        print("1. Full Name")
        print("2. Grades")
        print("3. ECA Activities")
        print("0. Cancel")
        choice = input("Enter choice: ")

        if choice == "1":
            new_name = input("Enter new full name: ")
            with open("users.txt", "w") as f:
                for line in users:
                    u, name, role = line.strip().split(",")
                    if u == username:
                        f.write(f"{u},{new_name},{role}\n")
                    else:
                        f.write(line)
            print("✅ Full name updated.")

        elif choice == "2":
            print("Enter new grades for 5 subjects:")
            grades = []
            for i in range(1, 6):
                grade = input(f"Subject {i}: ")
                grades.append(grade)
            with open("grades.txt", "r") as f:
                lines = f.readlines()
            with open("grades.txt", "w") as f:
                for line in lines:
                    u, g = line.strip().split(":")
                    if u == username:
                        f.write(f"{u}:{','.join(grades)}\n")
                    else:
                        f.write(line)
            print("✅ Grades updated.")

        elif choice == "3":
            print("Enter ECA activities separated by commas (e.g. football,debate):")
            eca_input = input("New activities: ")
            with open("eca.txt", "r") as f:
                lines = f.readlines()
            with open("eca.txt", "w") as f:
                for line in lines:
                    u, e = line.strip().split(":")
                    if u == username:
                        f.write(f"{u}:{eca_input}\n")
                    else:
                        f.write(line)
            print("✅ ECA activities updated.")

        elif choice == "0":
            print("Cancelled.")
        else:
            print("❌ Invalid choice.")
    def delete_student(self):
        print("\n== Delete Student ==")
        username = input("Enter student username to delete: ")

    # Step 1: Confirm student exists
        found = False
        with open("users.txt", "r") as f:
            users = f.readlines()
        for line in users:
            if line.startswith(username + ",") and ",student" in line:
                found = True
                break

        if not found:
            print("❌ Student not found.")
            return

        confirm = input(f"Are you sure you want to delete '{username}'? (y/n): ").lower()
        if confirm != 'y':
            print("❎ Deletion cancelled.")
            return

    # Step 2: Remove from users.txt
        with open("users.txt", "w") as f:
            for line in users:
                if not line.startswith(username + ","):
                    f.write(line)

    # Step 3: Remove from grades.txt
        with open("grades.txt", "r") as f:
            grades = f.readlines()
        with open("grades.txt", "w") as f:
            for line in grades:
                if not line.startswith(username + ":"):
                    f.write(line)

    # Step 4: Remove from eca.txt
        with open("eca.txt", "r") as f:
            eca = f.readlines()
        with open("eca.txt", "w") as f:
            for line in eca:
                if not line.startswith(username + ":"):
                    f.write(line)

        print(f"✅ Student '{username}' has been deleted from the system.")

    def generate_reports(self):
        print("\n== 📊 Reports Dashboard ==")

    # 1. Average Grades per Subject
        try:
            with open("grades.txt", "r") as f:
                subject_totals = [0] * 5
                student_count = 0
                for line in f:
                    _, grade_data = line.strip().split(":")
                    grades = list(map(int, grade_data.split(",")))
                    for i in range(5):
                        subject_totals[i] += grades[i]
                    student_count += 1

                if student_count == 0:
                    print("No student grades to analyze.")
                else:
                    print("\n📘 Average Grades Per Subject:")
                    for i in range(5):
                        avg = subject_totals[i] / student_count
                        print(f"  Subject {i+1}: {avg:.2f}")

        except FileNotFoundError:
            print("❌ grades.txt not found.")

    # 2. Most Active Students in ECA
        try:
            activity_counts = {}
            with open("eca.txt", "r") as f:
                for line in f:
                    username, activities = line.strip().split(":")
                    activity_list = activities.split(",") if activities.strip() else []
                    activity_counts[username] = len(activity_list)

            if not activity_counts:
                print("No ECA data available.")
            else:
                max_eca = max(activity_counts.values())
                most_active = [u for u, count in activity_counts.items() if count == max_eca]

                print("\n🎯 Most Active Student(s) in ECA:")
                for student in most_active:
                    print(f"  {student} ({activity_counts[student]} activities)")

        except FileNotFoundError:
            print("❌ eca.txt not found.")


class Student(User):
    def __init__(self, username, fullname):
        super().__init__(username, fullname, "student")

    def student_menu(self):
        while True:
            print("\n== Student Menu ==")
            print("1. View Profile")
            print("2. View Grades")
            print("3. View ECA")
            print("4. Update Profile")
            print("0. Logout")
            choice = input("Enter choice: ")

            if choice == "1":
                self.view_profile()
            elif choice == "2":
                print("[Grades] - Coming soon...")
            elif choice == "3":
                print("[ECA] - Coming soon...")
            elif choice == "4":
                print("[Update Profile] - Coming soon...")
            elif choice == "0":
                print("Logging out...")
                break
            else:
                print("Invalid choice. Try again.")
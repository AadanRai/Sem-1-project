#Here's the code to implement the login system:


from user import Admin, Student

def load_users():
    users = {}
    try:
        with open("users.txt", "r") as f:
            for line in f:
                username, fullname, role = line.strip().split(",")
                users[username] = {"fullname": fullname, "role": role}
    except FileNotFoundError:
        print("users.txt not found.")
    return users

def load_passwords():
    passwords = {}
    try:
        with open("passwords.txt", "r") as f:
            for line in f:
                username, password = line.strip().split(",")
                passwords[username] = password
    except FileNotFoundError:
        print("passwords.txt not found.")
    return passwords

def login(users, passwords):
    print("== Student Profile Management System ==")
    while True:
        username = input("Username: ")
        password = input("Password: ")

        if username in passwords and passwords[username] == password:
            print(f"\n✅ Welcome {users[username]['fullname']}!")
            return username, users[username]['role']
        else:
            print("❌ Invalid credentials. Try again.\n")

if __name__ == "__main__":
    try:
        users = load_users()
        passwords = load_passwords()
        if not users or not passwords:
            print("User or password data missing.")
        else:
            username, role = login(users, passwords)
            print(f"You are logged in as: {role}")

            # After successful login, instantiate User objects
            if role == "admin":
                admin = Admin(username, users[username]['fullname'])
                admin.admin_menu()
            elif role == "student":
                student = Student(username, users[username]['fullname'])
                student.student_menu()
                #What This Does:
# When the user logs in, it checks their role.

# If they’re admin: it creates an Admin object and opens the admin menu.

# If they’re a student: it creates a Student object and opens the student menu.

# Menus have placeholder options for now (coming soon...).
    
    except Exception as e:
        print(f"Error occurred: {e}")
        input("Press Enter to exit...")  # Keeps the console open for you to read the error




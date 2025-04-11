import tkinter as tk
from tkinter import messagebox, simpledialog
from analytics import run_analytics_dashboard

class AdminDashboard:
    def __init__(self, username, fullname):
        self.username = username
        self.fullname = fullname
        self.root = tk.Tk()
        self.root.title("Admin Dashboard")
        self.root.geometry("500x500")

        tk.Label(self.root, text=f"Welcome, {fullname}", font=("Arial", 18, "bold")).pack(pady=10)

        tk.Button(self.root, text="Add Student", command=self.add_student, width=30).pack(pady=5)
        tk.Button(self.root, text="Update Student", command=self.update_student, width=30).pack(pady=5)
        tk.Button(self.root, text="Delete Student", command=self.delete_student, width=30).pack(pady=5)
        tk.Button(self.root, text="View Student", command=self.view_student, width=30).pack(pady=5)
        tk.Button(self.root, text="Generate Reports", command=run_analytics_dashboard, width=30).pack(pady=5)
        tk.Button(self.root, text="Logout", command=self.root.destroy, fg="red", width=30).pack(pady=20)

        self.root.mainloop()

    def add_student(self):
        username = simpledialog.askstring("Add Student", "Enter Username:")
        fullname = simpledialog.askstring("Add Student", "Enter Full Name:")
        role = "student"

        if not username or not fullname:
            messagebox.showerror("Error", "Username and Fullname are required.")
            return

        try:
            with open("users.txt", "r") as f:
                for line in f:
                    if line.startswith(username + ","):
                        messagebox.showerror("Error", "Username already exists!")
                        return

            with open("users.txt", "a") as f:
                f.write(f"{username},{fullname},{role}\n")
            with open("grades.txt", "a") as f:
                f.write(f"{username}:0,0,0,0,0\n")
            with open("eca.txt", "a") as f:
                f.write(f"{username}:\n")

            messagebox.showinfo("Success", f"Student '{fullname}' added!")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_student(self):
        username = simpledialog.askstring("Update Student", "Enter student username:")
        if not username:
            return

        # Validate student exists
        try:
            with open("users.txt", "r") as f:
                lines = f.readlines()
                for line in lines:
                    u, _, role = line.strip().split(",")
                    if u == username and role == "student":
                        break
                else:
                    messagebox.showerror("Error", "Student not found.")
                    return
        except FileNotFoundError:
            messagebox.showerror("Error", "users.txt not found.")
            return

        option = simpledialog.askstring("Update", "What do you want to update?\n1: Full Name\n2: Grades\n3: ECA Activities")
        if option == "1":
            new_name = simpledialog.askstring("Update Name", "Enter new full name:")
            if new_name:
                with open("users.txt", "w") as f:
                    for line in lines:
                        u, name, role = line.strip().split(",")
                        if u == username:
                            f.write(f"{u},{new_name},{role}\n")
                        else:
                            f.write(line)
                messagebox.showinfo("Success", "Full name updated.")

        elif option == "2":
            grades = []
            for i in range(1, 6):
                g = simpledialog.askinteger("Grades", f"Enter grade for Subject {i}:", minvalue=0, maxvalue=100)
                grades.append(str(g))
            with open("grades.txt", "r") as f:
                grade_lines = f.readlines()
            with open("grades.txt", "w") as f:
                for line in grade_lines:
                    u, g = line.strip().split(":")
                    if u == username:
                        f.write(f"{u}:{','.join(grades)}\n")
                    else:
                        f.write(line)
            messagebox.showinfo("Success", "Grades updated.")

        elif option == "3":
            activities = simpledialog.askstring("ECA", "Enter ECA activities (comma-separated):")
            if activities is not None:
                with open("eca.txt", "r") as f:
                    eca_lines = f.readlines()
                with open("eca.txt", "w") as f:
                    for line in eca_lines:
                        u, a = line.strip().split(":")
                        if u == username:
                            f.write(f"{u}:{activities}\n")
                        else:
                            f.write(line)
                messagebox.showinfo("Success", "ECA updated.")
        else:
            messagebox.showinfo("Cancelled", "Update cancelled.")

    def delete_student(self):
        username = simpledialog.askstring("Delete Student", "Enter username to delete:")
        if not username:
            return

        confirm = messagebox.askyesno("Confirm", f"Are you sure you want to delete '{username}'?")
        if not confirm:
            return

        try:
            with open("users.txt", "r") as f:
                user_lines = f.readlines()
            with open("users.txt", "w") as f:
                for line in user_lines:
                    if not line.startswith(username + ","):
                        f.write(line)

            with open("grades.txt", "r") as f:
                grade_lines = f.readlines()
            with open("grades.txt", "w") as f:
                for line in grade_lines:
                    if not line.startswith(username + ":"):
                        f.write(line)

            with open("eca.txt", "r") as f:
                eca_lines = f.readlines()
            with open("eca.txt", "w") as f:
                for line in eca_lines:
                    if not line.startswith(username + ":"):
                        f.write(line)

            messagebox.showinfo("Deleted", f"Student '{username}' deleted.")
        except FileNotFoundError as e:
            messagebox.showerror("Error", str(e))

    def view_student(self):
        username = simpledialog.askstring("View Student", "Enter student username:")
        if not username:
            return

        try:
            found = False
            output = ""
            with open("users.txt", "r") as f:
                for line in f:
                    u, name, role = line.strip().split(",")
                    if u == username and role == "student":
                        output += f"👤 Name: {name}\n🆔 ID: {u}\n🎓 Role: {role}\n"
                        found = True
                        break
            if not found:
                messagebox.showerror("Not Found", "Student not found.")
                return

            # Load grades
            with open("grades.txt", "r") as f:
                for line in f:
                    u, data = line.strip().split(":")
                    if u == username:
                        grades = data.split(",")
                        output += "\n📘 Grades:\n"
                        for i, g in enumerate(grades, 1):
                            output += f"  Subject {i}: {g}\n"
                        break

            # Load ECA
            with open("eca.txt", "r") as f:
                for line in f:
                    u, data = line.strip().split(":")
                    if u == username:
                        ecas = data.split(",") if data.strip() else []
                        output += "\n🎯 ECA Activities:\n"
                        output += "\n".join(f"  - {a}" for a in ecas) if ecas else "  None"
                        break

            messagebox.showinfo("Student Info", output)

        except FileNotFoundError as e:
            messagebox.showerror("Error", str(e))


    def generate_reports(self):
        # This is where you would trigger your analytics
        print("Generating reports...")
        # Call the function to show analytics dashboard (if needed)
        run_analytics_dashboard()
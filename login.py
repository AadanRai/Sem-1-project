from tkinter import *
from PIL import Image, ImageTk

class login_system:
    def __init__(self, root):
        self.root = root
        self.root.title("login system")
        self.root.geometry("1100x600")
        self.root.config(bg="white")

        # === static image ========
        image = Image.open("ok.png")
        self.photo = ImageTk.PhotoImage(image)
        img_label = Label(self.root, image=self.photo, bg="white")
        img_label.place(x=10, y=100)

        # === Login frame ===
        login_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        login_frame.place(x=600, y=90, width=350, height=350)

        title1 = Label(login_frame, text="Welcome", font=("Elephant", 30, "bold"), bg="white")
        title1.place(x=0, y=30, relwidth=1)

        title2 = Label(login_frame, text="Login to your account to continue", font=("times new roman", 12), bg="white", fg="#767171")
        title2.place(x=0, y=75, relwidth=1)

        #==username and passsword lbl====
        lbl_user = Label(login_frame, text="Username", font=("times new roman", 15, "bold"), bg="white", fg="#767171")
        lbl_user.place(x=50, y=100)
        self.txt_username = Entry(login_frame, font=("times new roman", 15, "bold"), bg="lightgray")
        self.txt_username.place(x=50, y=140, width=250)

        lbl_pass = Label(login_frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="#767171")
        lbl_pass.place(x=50, y=170)
        self.txt_password = Entry(login_frame, font=("times new roman", 15, "bold"), bg="lightgray", show="*")
        self.txt_password.place(x=50, y=205, width=250)

        #==login button lbl===
        btn_login = Button(login_frame, text="Log in", font=("arial rounded mt bold", 15), bg="black", activebackground="white", fg="white")
        btn_login.place(x=75, y=300, width=200, height=35)

        hr = Label(login_frame, bg="lightgray")
        hr.place(x=50, y=250, width=250, height=2)

        #==or lbl==
        or_ = Label(login_frame, text="OR", bg="white", font=("times new roman", 12, "bold"))
        or_.place(x=155, y=240)

        #==forgot pass lbl===
        btn_forgot_ = Button(login_frame, text="forget password?", font=("times new roman", 10, "bold"), bg="white", fg="black", bd=0)
        btn_forgot_.place(x=125, y=270)

        # === Animation images ===
        self.im1 = ImageTk.PhotoImage(Image.open("ok3.webp").resize((369, 220)))
        self.im2 = ImageTk.PhotoImage(Image.open("ok2.webp").resize((369, 220)))
        self.image = self.im1  # Set initial image

        self.lbl_change_Image = Label(self.root, bg="white")
        self.lbl_change_Image.place(x=146, y=134, width=369, height=220)

        # Start animation
        self.animate()

    def animate(self):
        # Toggle image
        self.image = self.im2 if self.image == self.im1 else self.im1
        self.lbl_change_Image.configure(image=self.image)
        self.lbl_change_Image.image = self.image  # Keep reference
        self.root.after(2000, self.animate)

# Run app
root = Tk()
obj = login_system(root)
root.mainloop()

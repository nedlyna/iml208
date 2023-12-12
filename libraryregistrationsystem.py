import tkinter as tk
from tkinter import messagebox

class Student:
    def __init__(self, fullname, faculty, matric_number, semester, username, password, gender, university_type, phone_number, email):
        self.fullname = fullname
        self.faculty = faculty
        self.matric_number = matric_number
        self.semester = semester
        self.username = username
        self.password = password
        self.gender = gender
        self.university_type = university_type
        self.phone_number = phone_number
        self.email = email

class RegistrationSystemGUI:
    def __init__(self, master):
        self.master = master
        master.title("Student Registration System")
        self.master.geometry("890x800")
        master.configure(bg="#013220")

        self.registration_frame = tk.Frame(master, bg='#1b4d3e')
        self.login_frame = tk.Frame(master, bg='#1b4d3e')
        self.action_frame = tk.Frame(master, bg='#1b4d3e')

        self.setup_registration_frame()
        self.setup_login_frame()
        self.setup_action_frame()

        self.show_registration_frame()

        self.students = []

    def setup_registration_frame(self):
        self.label_title = tk.Label(self.registration_frame, text="REGISTRATION FORM", font=("Helvetica", 35), bg='#1b4d3e', fg='white')
        self.label_fullname = tk.Label(self.registration_frame, text="Full Name:", font=("Palatino", 12), bg='#1b4d3e', fg='white')
        self.label_faculty = tk.Label(self.registration_frame, text="Faculty:", font=("Palatino", 12), bg='#1b4d3e', fg='white')
        self.label_matric_number = tk.Label(self.registration_frame, text="Matric Number:", font=("Palatino", 12), bg='#1b4d3e', fg='white')
        self.label_semester = tk.Label(self.registration_frame, text="Semester:", font=("Palatino", 12), bg='#1b4d3e', fg='white')
        self.label_gender = tk.Label(self.registration_frame, text="Gender:", font=("Palatino", 12), bg='#1b4d3e', fg='white')
        self.label_university_type = tk.Label(self.registration_frame, text="University Type:", font=("Palatino", 12), bg='#1b4d3e', fg='white')
        self.label_username = tk.Label(self.registration_frame, text="Username:", font=("Palatino", 12), bg='#1b4d3e', fg='white')
        self.label_password = tk.Label(self.registration_frame, text="Password:", font=("Palatino", 12), bg='#1b4d3e', fg='white')
        self.label_phone_number = tk.Label(self.registration_frame, text="Phone Number:", font=("Palatino", 12), bg='#1b4d3e', fg='white')
        self.label_email = tk.Label(self.registration_frame, text="Email:", font=("Palatino", 12), bg='#1b4d3e', fg='white')

        self.entry_fullname = tk.Entry(self.registration_frame)
        self.entry_faculty = tk.Entry(self.registration_frame)
        self.entry_matric_number = tk.Entry(self.registration_frame)
        self.entry_semester = tk.Entry(self.registration_frame)
        self.gender_var = tk.StringVar()
        self.gender_var.set("Male")
        self.gender_menu = tk.OptionMenu(self.registration_frame, self.gender_var, "Male", "Female")
        self.university_type_var = tk.StringVar()
        self.university_type_var.set("Government")
        self.university_type_menu = tk.OptionMenu(self.registration_frame, self.university_type_var, "Government", "Private")
        self.entry_username = tk.Entry(self.registration_frame)
        self.entry_password = tk.Entry(self.registration_frame, show="*")
        self.entry_phone_number = tk.Entry(self.registration_frame)
        self.entry_email = tk.Entry(self.registration_frame)


        self.button_register = tk.Button(self.registration_frame, text="Register", font=("Helvetica", 12), command=self.register_student)

        self.label_title.grid(row=0, column=0, pady=12, sticky="ew")
        self.label_fullname.grid(row=1, column=0, sticky="e")
        self.entry_fullname.grid(row=1, column=1, sticky="w")
        self.label_faculty.grid(row=2, column=0, sticky="e")
        self.entry_faculty.grid(row=2, column=1, sticky="w")
        self.label_matric_number.grid(row=3, column=0, sticky="e")
        self.entry_matric_number.grid(row=3, column=1, sticky="w")
        self.label_semester.grid(row=4, column=0, sticky="e")
        self.entry_semester.grid(row=4, column=1, sticky="w")
        self.label_gender.grid(row=5, column=0, sticky="e")
        self.gender_menu.grid(row=5, column=1, sticky="w")
        self.label_university_type.grid(row=6, column=0, sticky="e")
        self.university_type_menu.grid(row=6, column=1, sticky="w")
        self.label_username.grid(row=7, column=0, sticky="e")
        self.entry_username.grid(row=7, column=1, sticky="w")
        self.label_password.grid(row=8, column=0, sticky="e")
        self.entry_password.grid(row=8, column=1, sticky="w")
        self.label_phone_number.grid(row=10, column=0, sticky="e")
        self.entry_phone_number.grid(row=10, column=1, sticky="w")
        self.label_email.grid(row=11, column=0, sticky="e")
        self.entry_email.grid(row=11, column=1, sticky="w")
        self.button_register.grid(row=12, column=1, pady=10)

    def setup_login_frame(self):
        self.label_login_username = tk.Label(self.login_frame, text="Username:", font=("Palatino", 12),bg='#1b4d3e', fg='white' )
        self.label_login_password = tk.Label(self.login_frame, text="Password:", font=("Palatino", 12),bg='#1b4d3e', fg='white' )

        self.entry_login_username = tk.Entry(self.login_frame)
        self.entry_login_password = tk.Entry(self.login_frame, show="*")

        self.button_login = tk.Button(self.login_frame, text="Login", font=("Helvetica", 12), command=self.login_student)

        self.label_title.grid(row=0, column=1, pady=10, sticky="w")
        self.label_login_username.grid(row=1, column=0, sticky="e")
        self.entry_login_username.grid(row=1, column=1, sticky="w")
        self.label_login_password.grid(row=2, column=0, sticky="e")
        self.entry_login_password.grid(row=2, column=1, sticky="w")
        self.button_login.grid(row=3, column=1, pady=10)

    def setup_action_frame(self):
        self.label_action_username = tk.Label(self.action_frame, text="Username:", font=("Palatino", 12), bg='#1b4d3e', fg='white')
        self.label_action_password = tk.Label(self.action_frame, text="Password:", font=("Palatino", 12),bg='#1b4d3e', fg='white' )

        self.entry_action_username = tk.Entry(self.action_frame)
        self.entry_action_password = tk.Entry(self.action_frame, show="*")

        self.button_update = tk.Button(self.action_frame, text="Update Data", font=("Helvetica", 12), command=self.update_data)
        self.button_delete = tk.Button(self.action_frame, text="Delete Data", font=("Helvetica", 12), command=self.delete_data)
        self.button_view = tk.Button(self.action_frame, text="View Data", font=("Helvetica", 12), command=self.view_data)

        self.label_action_username.pack()
        self.entry_action_username.pack()
        self.label_action_password.pack()
        self.entry_action_password.pack()
        self.button_update.pack(side=tk.LEFT)
        self.button_delete.pack(side=tk.RIGHT)
        self.button_view.pack()

    def show_registration_frame(self):
        self.login_frame.pack_forget()
        self.action_frame.pack_forget()
        self.registration_frame.pack()

    def show_login_frame(self):
        self.registration_frame.pack_forget()
        self.action_frame.pack_forget()
        self.login_frame.pack()

    def show_action_frame(self):
        self.registration_frame.pack_forget()
        self.login_frame.pack_forget()
        self.action_frame.pack()

    def register_student(self):
        fullname = self.entry_fullname.get()
        faculty = self.entry_faculty.get()
        matric_number = self.entry_matric_number.get()
        semester = self.entry_semester.get()
        gender = self.gender_var.get()
        university_type = self.university_type_var.get()
        username = self.entry_username.get()
        password = self.entry_password.get()
        phone_number = self.entry_phone_number.get()
        email = self.entry_email.get()


        if all([fullname, faculty, matric_number, semester, username, password, university_type, phone_number, email]):
            new_student = Student(fullname, faculty, matric_number, semester, username, password, gender, university_type, phone_number, email)
            self.students.append(new_student)
            messagebox.showinfo("Registration Successful", f"Student {fullname} registered successfully!")
            self.show_login_frame()
        else:
            messagebox.showwarning("Registration Error", "Please fill in all fields.")


    def login_student(self):
        login_username = self.entry_login_username.get()
        login_password = self.entry_login_password.get()

        if any(student.username == login_username and student.password == login_password for student in self.students):
            messagebox.showinfo("Login Successful", f"Welcome back, {login_username}!")
            self.show_action_frame()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password. Please check your credentials.")

    def update_data(self):
        action_username = self.entry_action_username.get()
        action_password = self.entry_action_password.get()

        for student in self.students:
            if student.username == action_username and student.password == action_password:
                updated_fullname = input("Enter updated Full Name: ")
                updated_faculty = input("Enter updated Faculty: ")
                updated_semester = input("Enter updated Semester: ")
               
                student.fullname = updated_fullname
                student.faculty = updated_faculty
                student.semester = updated_semester


                messagebox.showinfo("Update Successful", f"Data for {action_username} updated successfully!")
                break
        else:
            messagebox.showerror("Update Failed", "Invalid username or password. Please check your credentials.")

    def delete_data(self):
        action_username = self.entry_action_username.get()
        action_password = self.entry_action_password.get()

        for student in self.students:
            if student.username == action_username and student.password == action_password:
                self.students.remove(student)
                messagebox.showinfo("Deletion Successful", f"Data for {action_username} deleted successfully!")
                break
        else:
            messagebox.showerror("Deletion Failed", "Invalid username or password. Please check your credentials.")

    def view_data(self):
        action_username = self.entry_action_username.get()
        action_password = self.entry_action_password.get()

        for student in self.students:
            if student.username == action_username and student.password == action_password:
                data_message = f"Full Name: {student.fullname}\nFaculty: {student.faculty}\nMatric Number: {student.matric_number}\nSemester: {student.semester}\nGender: {student.gender}\nUniversity: {student.university_type}\nPhone number: {student.phone_number}\nEmail: {student.email}"
                messagebox.showinfo("Student Data", data_message)
                break
        else:
            messagebox.showerror("View Data Failed", "Invalid username or password. Please check your credentials.")


def main():
    root = tk.Tk()
    app = RegistrationSystemGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

from tkinter import *
from PIL import ImageTk, Image
import pyodbc
import tkinter.messagebox as mb


class LoginPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Login Page')

        # ========================================================================
        # ============================background image============================
        # ========================================================================
        self.bg_frame = Image.open('Reg_Images\\background1.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
        # ====== Login Frame =========================
        self.lgn_frame = Frame(self.window, bg='#040405', width=950, height=600)
        self.lgn_frame.place(x=200, y=70)

        # ========================================================================
        # ========================================================
        # ========================================================================
        self.txt = "STUDENT REGISTRATION"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#040405",
                             fg='white',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=155, y=30, width=700, height=30)

        # ========================================================================
        # ============ Left Side Image ================================================
        # ========================================================================
        '''
        self.side_image = Image.open('images\\vector.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=100)
        '''

        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================
        self.sign_in_image = Image.open('Reg_Images\\hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=400, y=110)

        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
        self.sign_in_label = Label(self.lgn_frame, text="Registration", bg="#040405", fg="white",
                                   font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=415, y=240)

        # ========================================================================
        # ============================username====================================
        # ========================================================================
        self.name_label = Label(self.lgn_frame, text="Student Name", bg="#040405", fg="white",
                                font=("yu gothic ui", 13, "bold"))
        self.name_label.place(x=95, y=300)

        self.name_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                font=("yu gothic ui ", 12, "bold"))
        self.name_entry.place(x=130, y=335, width=270)

        self.name_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.name_line.place(x=100, y=359)
        # =============================department=======================================
        self.dep_label = Label(self.lgn_frame, text="Department", bg="#040405", fg="white",
                                  font=("yu gothic ui", 13, "bold"))
        self.dep_label.place(x=95, y=380)

        self.dep_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                  font=("yu gothic ui ", 12, "bold"))
        self.dep_entry.place(x=130, y=420, width=270)

        self.dep_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.dep_line.place(x=100, y=440)
        # =============================rollno=========================================

        self.rollno_label = Label(self.lgn_frame, text="RollNo", bg="#040405", fg="white",
                                  font=("yu gothic ui", 13, "bold"))
        self.rollno_label.place(x=550, y=300)

        self.rollno_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                  font=("yu gothic ui ", 12, "bold"))
        self.rollno_entry.place(x=580, y=335, width=270)

        self.rollno_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.rollno_line.place(x=550, y=359)
        # =============================================year=========================
        self.year_label = Label(self.lgn_frame, text="Year", bg="#040405", fg="white",
                                font=("yu gothic ui", 13, "bold"))
        self.year_label.place(x=550, y=380)

        self.year_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                font=("yu gothic ui", 12, "bold"))
        self.year_entry.place(x=580, y=416, width=244)

        self.year_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.year_line.place(x=550, y=440)
        # ===== Username icon =========
        '''
        self.username_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=332)
        '''

        # ========================================================================
        # ============================login button================================
        # ========================================================================

        # ========================================================================
        # ============================Forgot password=============================
        # ========================================================================


        def store(roll, student, dep, stud_year):

                conn = pyodbc.connect(
                    'DRIVER=ODBC Driver 17 for SQL Server;Server=USER-PC;Database=attendance_db;Trusted_Connection=Yes;')
                cursor = conn.cursor()
                sql = '''insert into attendance_db.dbo.personal_details(rollno,stud_name,department,stud_year) values(?,?,?,?)'''
                val = (roll, student, dep, stud_year)
                cursor.execute(sql, val)
                conn.commit()

        def condition():
            student_name = self.name_entry.get()
            rollno = self.rollno_entry.get()
            department = self.dep_entry.get()
            year = self.year_entry.get()

            if student_name != "" or rollno != "" or department != "" or year != "":
                store(rollno,student_name,department,year)
            else:
                mb.showinfo('Information', "Please enter all the details")


        self.lgn_button = Image.open('Reg_Images\\btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=340, y=465)
        self.login = Button(self.lgn_button_label, text='SUBMIT', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white', command=condition)
        self.login.place(x=20, y=10)

        '''
        self.forgot_button = Button(self.lgn_frame, text="Forgot Password ?",
                                    font=("yu gothic ui", 13, "bold underline"), fg="white", relief=FLAT,
                                    activebackground="#040405"
                                    , borderwidth=0, background="#040405", cursor="hand2")
        self.forgot_button.place(x=630, y=510)

        # =========== Sign Up ==================================================
        self.sign_label = Label(self.lgn_frame, text='No account yet?', font=("yu gothic ui", 11, "bold"),
                                relief=FLAT, borderwidth=0, background="#040405", fg='white')
        self.sign_label.place(x=550, y=560)

        self.signup_img = ImageTk.PhotoImage(file='images\\register.png')
        self.signup_button_label = Button(self.lgn_frame, image=self.signup_img, bg='#98a65d', cursor="hand2",
                                          borderwidth=0, background="#040405", activebackground="#040405")
        self.signup_button_label.place(x=670, y=555, width=111, height=35)
     '''
        # ========================================================================
        # ============================Year====================================
        # ========================================================================

        # ======== Password icon ================
        '''
        self.password_icon = Image.open('images\\password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=414)
        # ========= show/hide password ==================================================================
        self.show_image = ImageTk.PhotoImage \
            (file='images\\show.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='images\\hide.png')

        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=860, y=420)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)
        self.password_entry.config(show='*')
    '''



def page():
    window = Tk()
    LoginPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()
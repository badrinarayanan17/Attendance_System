from tkinter import *
from tkinter import messagebox as mb
import pyttsx3
import subprocess
import datetime
import pyodbc
from datetime import datetime as date




root = Tk()
root.title('Login')
root.geometry('1280x800')
root.configure(bg="#E5C2C0")
root.resizable(False, False)
'''
welcome_voice = pyttsx3.init()
welcome_voice.setProperty("rate", 130)
welcome_voice.say('WELCOME TO AUTOMATIC ATTENDANCE REGISTRATION SYSTEM')
welcome_voice.runAndWait()

'''

def signin():

    username = user.get()
    password3 = password.get()

    if username == 'admin' and password3 == 'admin':
        welcome_voice = pyttsx3.init()
        welcome_voice.setProperty("rate", 130)
        welcome_voice.say('Login Sucessfull , Read the instructions in upcoming page')
        welcome_voice.runAndWait()
        screen = Toplevel(root)
        screen.title("Instructions")
        screen.geometry('1280x800')
        screen.configure(bg="white")
        img2 = PhotoImage(file='C:\\Users\\User\\Downloads\\instruction.png')
        Label(screen, image=img2, bg="white").place(x=0, y=130)
        heading2 = Label(screen, text='WELCOME TO AUTOMATIC ATTENDANCE REGISTRATION SYSTEM', fg='black',bg='white',
                         font=('Candara', 22,'bold'))
        heading2.place(x=243, y=50)
        frame = Frame(screen, width=590, height=400, bg="white")
        frame.place(x=640,y=180)
        ins1 = Label(frame, text='1) Instruct the students to show their face infront of the webcam for one second', fg='black', bg='white',
                         font=('Candara', 13))
        ins1.place(x=0, y=10)
        ins2 = Label(frame, text='2) Student face will be automatically detected',fg='black', bg='white', font=('Candara', 13))
        ins2.place(x=0, y=60)
        ins3 = Label(frame, text='3) Finally the attendance will be stored in your own database ', fg='black', bg='white',
                     font=('Candara', 13))
        ins3.place(x=0, y=110)
        img3 = PhotoImage(file='C:\\Users\\User\\OneDrive\\Desktop\\Mini-Project\\Detectimg.png')
        Label(frame, image=img3, bg='#E5C2C0').place(x=0, y=160)

        crctDate = datetime.datetime.now().date()

        def startfunc():
            cmd = 'python main.py'
            p = subprocess.Popen(cmd, shell=True)
            Out, err = p.communicate()
            print(err)
            print(Out)



        def showattendance():

            conn = pyodbc.connect(
                'DRIVER=ODBC Driver 17 for SQL Server;Server=USER-PC;Database=attendance_db;Trusted_Connection=Yes;')
            cursor = conn.cursor()

            '''
            sql = 
            select dbo.mark_attendance.rollno ,dbo.personal_details.stud_name,dbo.personal_details.department,dbo.personal_details.stud_year,dbo.mark_attendance.InDate,dbo.mark_attendance.InTime,dbo.mark_attendance.current_day
            from dbo.personal_details as PD full outer join dbo.mark_attendance as MA
            on PD.rollno = MA.rollno
            '''

            cursor.execute("select * from view1")

            for row in cursor.fetchall():
                print(row)

            print("Data Printed successfully")
            conn.commit()

        Button(screen, width=39, pady=7, text='Show Registry', bg='black', fg='white', border=0,
                   command=showattendance).place(x=100,
                                            y=630)

        Button(screen, width=39, pady=7, text='Start Recording Attendance', bg='black', fg='white', border=0,command=startfunc).place(x=420,
                                                                                                                 y=630)
        screen.mainloop()
    elif username != 'admin' and password3 != 'admin':
        welcome_voice = pyttsx3.init()
        welcome_voice.setProperty("rate", 130)
        welcome_voice.say('Invalid Username and Password')
        welcome_voice.runAndWait()
        mb.showerror("Invalid", "Invalid Username and Password")


img = PhotoImage(file='C:\\Users\\User\\Downloads\\login.png')
Label(root, image=img, bg='#E5C2C0').place(x=200, y=200)  # 50 and 50

heading1 = Label(root, text='AUTOMATIC  ATTENDANCE  REGISTRATION  SYSTEM', fg='black', bg='#E5C2C0',
                 font=('Candara', 24,'bold'))
heading1.place(x=270, y=10)
frame = Frame(root, width=350, height=350, bg="#E5C2C0")
frame.place(x=675, y=230)  # 480 and 70


heading = Label(frame, text='SIGN IN', fg='black', bg='#E5C2C0', font=('Candara', 22))
heading.place(x=100, y=5)



# -----------------------------------UserName---------------------------
def enteron(e):
    user.delete(0, 'end')


def leaveon(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')


user = Entry(frame, width=25, fg='black', border=0, bg='#E5C2C0', font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', enteron)
user.bind('<FocusOut>', leaveon)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)


# ------------------------------------Password------------------------------
def enteron(e):
    password.delete(0, 'end')


def leaveon(e):
    password1 = password.get()
    if password1 == '':
        password.insert(0, 'Password')



password = Entry(frame, width=25, fg='black', border=0, bg='#E5C2C0' ,font=('Microsoft YaHei UI Light', 11))
password.place(x=30, y=150)
password.insert(0, 'Password')
password.bind('<FocusIn>', enteron)
password.bind('<FocusOut>', leaveon)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)
# ------------------------------------Submit---------------------------
Button(frame, width=39, pady=7, text='Sign in', bg='black', fg='white', border=0, command=signin).place(x=35, y=204)
label = Label(frame, text="Click to Sign In ", fg='black', bg='#E5C2C0', font=('Microsoft YaHei UI Light', 9))
label.place(x=130, y=255)



root.mainloop()



'''
root = Tk()
root.title('Login Page')
root.geometry("1280x800")
root.configure(bg = '#fff')
root.resizable(False,False)

img = PhotoImage(file='C:\\Users\\User\\Downloads\\login.png')
Label(root,image=img,bg="white").place(x=200,y=200)

frame = Frame(root,width=350,height=350,bg = "white")
frame.place(x=700,y=180)

head = Label(frame,text= 'SIGN IN',fg='#57a1f8',bg='white',font=('Times new Roman',20,'bold'))
head.place(x=100,y=5)

'----------'
user = Entry(frame,width=25,fg='black',border= 0,bg='white',font=('Microsoft yaHei UI Light',11))
user.place(x=40,y=82)
user.insert(0,'Username')
Frame(frame,width=295,height=2,bg='black').place(x=40,y=110)
'----------'
unique = Entry(frame,width=25,fg='black',border= 0,bg='white',font=('Microsoft yaHei UI Light',11))
unique.place(x=40,y=150)
unique.insert(0,'Password')
Frame(frame,width=295,height=2,bg='black').place(x=40,y=177)



root.mainloop()
'''
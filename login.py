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
def register():
    rootreg = Tk()
    rootreg.title('Sign Up')
    rootreg.geometry('900x600')
    rootreg.configure(bg="#E5C2C0")
    rootreg.resizable(False, False)
    heading1 = Label(rootreg, text='REGISTER NEW USER', fg='black', bg='#E5C2C0',
                     font=('Candara', 24, 'bold'))
    heading1.place(x=150, y=300)
    frame = Frame(rootreg, width=350, height=400, bg="#E5C2C0")
    frame.place(x=500, y=190)  # 480 and 70
    heading = Label(frame, text='SIGN UP', fg='black', bg='#E5C2C0', font=('Candara', 22))
    heading.place(x=100, y=0)
    # -----------------------------------UserName---------------------------
    uslabel = Label(frame, text='Create Username', fg='black', bg='#E5C2C0', font=('Candara', 13))
    uslabel.place(x=30,y=55)
    userreg = Entry(frame, width=25, fg='black', border=0, bg='#E5C2C0', font=('Microsoft YaHei UI Light', 11))
    userreg.place(x=30, y=90)



    Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

    # ------------------------------------Password------------------------------

    uslabel = Label(frame, text='Create Password', fg='black', bg='#E5C2C0', font=('Candara', 13))
    uslabel.place(x=30, y=120)
    passwordreg = Entry(frame, width=25, fg='black', border=0, bg='#E5C2C0', font=('Microsoft YaHei UI Light', 11))
    passwordreg.place(x=30, y=150)



    Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)



    def regins():
        cusername = str(userreg.get())
        cpass = str(passwordreg.get())
        conn = pyodbc.connect(
            'DRIVER=ODBC Driver 17 for SQL Server;Server=USER-PC;Database=attendance_db;Trusted_Connection=Yes;')
        cursor = conn.cursor()
        sql = '''insert into attendance_db.dbo.register(userregname,userpassword) values('%s','%s')''' % (cusername,cpass)

        cursor.execute(sql)
        conn.commit()
        mb.showinfo('Signup','Registered Successfully')

    Button(frame, width=39, pady=7, text='Register', bg='green', fg='white', border=0, command=regins).place(x=35,
                                                                                                             y=204)


    rootreg.mainloop()




def signin():

    username = str(user.get())
    password3 = str(password.get())
    conn = pyodbc.connect(
        'DRIVER=ODBC Driver 17 for SQL Server;Server=USER-PC;Database=attendance_db;Trusted_Connection=Yes;')
    cursor = conn.cursor()
    sql = "SELECT * FROM attendance_db.dbo.register WHERE userregname = '" + username + "' AND userpassword = '" + password3 + "'"
    print(sql)
    cursor.execute(sql)
    rowcount = cursor.rowcount
    print(rowcount)
    conn.commit()
    if cursor.rowcount == -1:
        welcome_voice = pyttsx3.init()
        welcome_voice.setProperty("rate", 130)
        welcome_voice.say('Login Sucessfull , Read the instructions in upcoming page')
        welcome_voice.runAndWait()
        screen = Toplevel(root)
        screen.title("Instructions")
        screen.geometry('1280x800')
        screen.configure(bg="#E5C2C0")
        img2 = PhotoImage(file='C:\\Users\\User\\PycharmProject\\Mini_Project\\instruction.png')
        Label(screen, image=img2, bg="#E5C2C0").place(x=0, y=110)
        heading2 = Label(screen, text='WELCOME TO AUTOMATIC ATTENDANCE REGISTRATION SYSTEM', fg='black',bg="#E5C2C0",
                         font=('Candara', 22,'bold'))
        heading2.place(x=243, y=20)
        frame = Frame(screen, width=590, height=400, bg="#E5C2C0")
        frame.place(x=640,y=140)
        ins1 = Label(frame, text='1) Instruct the students to show their face infront of the webcam for one second', fg='black', bg="#E5C2C0",
                         font=('Candara', 13))
        ins1.place(x=0, y=10)
        ins2 = Label(frame, text='2) Student face will be automatically detected',fg='black', bg="#E5C2C0", font=('Candara', 13))
        ins2.place(x=0, y=60)
        ins3 = Label(frame, text='3) Finally the attendance will be stored in your own database ', fg='black', bg="#E5C2C0",
                     font=('Candara', 13))
        ins3.place(x=0, y=110)
        img3 = PhotoImage(file='C:\\Users\\User\\OneDrive\\Desktop\\Mini-Project\\Detectimg.png')
        Label(frame, image=img3, bg='#E5C2C0').place(x=0, y=160)



        def startfunc():
            cmd = 'python main.py'
            p = subprocess.Popen(cmd, shell=True)
            Out, err = p.communicate()
            print(err)
            print(Out)
        def outfunc():
            cmd = 'python main2.py'
            p = subprocess.Popen(cmd, shell=True)
            Out, err = p.communicate()
            print(err)
            print(Out)

        def regfunc():
            cmd = 'python Registration.py'
            p = subprocess.Popen(cmd, shell=True)
            Out, err = p.communicate()
            print(err)
            print(Out)


        def showattendance():

            conn = pyodbc.connect(
                'DRIVER=ODBC Driver 17 for SQL Server;Server=USER-PC;Database=attendance_db;Trusted_Connection=Yes;')
            cursor = conn.cursor()
            root2 = Tk()
            root2.geometry("1280x800")
            cursor.execute("SELECT * FROM view1")
            i = 0
            for student in cursor:
                for j in range(len(student)):
                    e = Entry(root2, width=10, fg='blue')
                    e.grid(row=i, column=j)
                    e.insert(END, student[j])
                i = i + 1
                e = Label(root2, width=35, text=student[j],
                          borderwidth=2, relief='ridge', anchor="w")
            root2.mainloop()

        def showoutattendance():

            conn = pyodbc.connect(
                    'DRIVER=ODBC Driver 17 for SQL Server;Server=USER-PC;Database=attendance_db;Trusted_Connection=Yes;')
            cursor = conn.cursor()
            root2 = Tk()
            root2.geometry("1280x800")
            cursor.execute("SELECT * FROM view2")
            i = 0
            for student in cursor:
                for j in range(len(student)):
                    e = Entry(root2, width=10, fg='blue')
                    e.grid(row=i, column=j)
                    e.insert(END, student[j])
                    i = i + 1
                    e = Label(root2, width=35, text=student[j],
                              borderwidth=2, relief='ridge', anchor="w")
                root2.mainloop()

            '''
            sql = 
            select dbo.mark_attendance.rollno ,dbo.personal_details.stud_name,dbo.personal_details.department,dbo.personal_details.stud_year,dbo.mark_attendance.InDate,dbo.mark_attendance.InTime,dbo.mark_attendance.current_day
            from dbo.personal_details as PD full outer join dbo.mark_attendance as MA
            on PD.rollno = MA.rollno
            

            cursor.execute("select * from view1")

            for row in cursor.fetchall():
                print(row)

            print("Data Printed successfully")
            '''
            conn.commit()

        def exitfunc():

            exit()

        Button(screen, width=39, pady=7, text='Register Student Details', bg='black', fg='white', border=0, command=regfunc).place(x=900,
                                                                                                                y=590)

        Button(screen, width=39, pady=7, text='Exit', bg='red', fg='white', border=0, command=exitfunc).place(x=900,
                             y=650)

        Button(screen, width=39, pady=7, text='Show Intime Registry', bg='black', fg='white', borderwidth=0,
                   command=showattendance).place(x=100,
                                            y=590)

        Button(screen, width=39, pady=7, text='Start Intime Attendance', bg='black', fg='white', border=0,command=startfunc).place(x=470,
                                                                                                                 y=590)


        Button(screen, width=39, pady=7, text='Show Outtime Registry', bg='black', fg='white', border=0,command=showoutattendance
               ).place(x=100,
                                             y=650)

        Button(screen, width=39, pady=7, text='Start Outtime Attendance', bg='black', fg='white', border=0,command=outfunc,
               ).place(x=470,
                                        y=650)
        screen.mainloop()

    else:
        welcome_voice = pyttsx3.init()
        welcome_voice.setProperty("rate", 130)
        welcome_voice.say('Invalid username and Password ')
        welcome_voice.runAndWait()
        mb.showinfo('Invalid','Invalid Credentials')


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


uslabel = Label(frame, text='Username', fg='black', bg='#E5C2C0', font=('Candara', 13))
uslabel.place(x=30,y=55)
user = Entry(frame, width=25, fg='black', border=0, bg='#E5C2C0', font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)



Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)


# ------------------------------------Password------------------------------



uslabel = Label(frame, text=' Password', fg='black', bg='#E5C2C0', font=('Candara', 13))
uslabel.place(x=30, y=120)
password = Entry(frame, width=25, fg='black', border=0, bg='#E5C2C0' ,font=('Microsoft YaHei UI Light', 11))
password.place(x=30, y=150)


Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)
# ------------------------------------Submit---------------------------
Button(frame, width=39, pady=7, text='Sign in', bg='green', fg='white', border=0, command=signin).place(x=35, y=204)
label = Label(frame, text=" Register New User? Click Below !", fg='black', bg='#E5C2C0', font=('Microsoft YaHei UI Light', 9))
label.place(x=70, y=255)

Button(frame, width=39, pady=7, text='Sign up', bg='red', fg='white', border=0, command=register).place(x=35, y=295)



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
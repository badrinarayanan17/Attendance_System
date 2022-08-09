'''
from getpass import getpass

count_num = 3
while count_num > 0:
    count = count_num -1
    username = input('Enter Username : ')
    password = getpass('Enter Password: ')

    if username == 'badri' and password == 'jovial':
     print('Login Successful')
    else:
     print('Login failed')
     print('You have %d valid attempts now '%(count_num))

        def showAttendance(crctDate):
            conn = pyodbc.connect(
                'DRIVER=ODBC Driver 17 for SQL Server;Server=USER-PC;Database=attendance_db;Trusted_Connection=Yes;')
            cursor = conn.cursor()
            cursor.execute("select ")
            conn.commit()
'''

from datetime import datetime as date

print(crctDay)
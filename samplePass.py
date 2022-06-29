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
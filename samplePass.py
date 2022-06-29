from getpass import getpass

count = 3
while count > 0:
    count = count -1
    username = input('Enter Username : ')
    password = getpass('Enter Password: ')

    if username == 'badri' and password == 'jovial':
     print('Login Successful')
    else:
     print('Login failed')
     print('You have %d valid attempts now '%(count))
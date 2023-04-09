class User:
    name = 'No Name Provided'
    email = ' '
    password = '1234abcd'
    account_number = 0

class Employee(User):
    base_pay = 20.25
    department = 'General'
    start_date = ' '

class Customer(User):
    mailing_address = ' '
    mailing_list = True
    birthdate = ' ' 

from classes.users import User

def menu():
    print('[0] Login')
    print('[1] Create User')

    try:
        option = int(input('Choose option: '))
    except:
        print('Invalid Option')
        menu()

    if option == 0:
        return login()
    if option == 1:
        return create_user()
    else:
        print('Invalid Option')
        menu()

def login():

    try:
        username = input('Username: ')
        password = input('Password: ') #TODO: when safely storing, decrypt?

        user = User(username=username, password=password, first_name=None, last_name=None).get()

        return user
    except:
        print('User {} not found with provided credentials'.format(username))


def create_user():
    try:
        username   = input('Username: ')
        password   = input('Password: ')
        first_name = input('First name (optional): ')
        last_name  = input('Last name (optional): ')

        user = User(username=username, password=password, first_name=first_name, last_name=last_name)

        user.create()

        return user
    except:
        print('Unable to create user')

def create_account():
    
    
def access(user):
    match user:
        case 'Admin' | 'Manager':
            print('Full access')
        case 'Guest':
            print('Limited Access')
        case _:
            print('No access')
user = input('Enter the user type: ')

access(user)
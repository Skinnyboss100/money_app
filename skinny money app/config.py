#THIS MODUULE SAVES EVERYTHING ABOUT THE USER


def save_fullname(fullname):
    with open('user_details.txt', 'w') as f:
        f.write(f'Full Name: {fullname}\n')
    print(f'Full name "{fullname}" has been saved.')
#THIS IS THE MODULE THAT SAVES THE DTAILS OF THE USER FOR USE BY THE APP
import time
from config import save_fullname

def ask_name():
    first_name = input('ENTER FIRST NAME : ')
    last_name = input('ENTER LAST NAME : ')
    fullname = f'{last_name} {first_name}'
    print(fullname)
    
    verification = input('Press y if it is your name and n if it is not your name : ').lower()
    if verification == 'y':
        save_fullname(fullname)
        time.sleep(3)
        print(f'WELCOME {fullname}')
    elif verification == 'n':
        ask_name()
    else:
        time.sleep(2)
        print('INVALID INPUT.....')
        ask_name()

ask_name()
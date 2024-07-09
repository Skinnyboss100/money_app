#THIS IS THE MODULE FOR COLLECTING AND ENCRYPTING THE PASSWORD

import time

def password_collector():
    password = input('Input your password : ')
    time.sleep(1)
    rewrite_password = input('Confirm password by rewriting it : ')
  
    if password != rewrite_password:
        print('THE PASSWORDS DO NOT TALLY...')
        password_collector()
        
    elif password == rewrite_password:
        time.sleep(2)
        print('PASSWORD CONFIRMED.....')
        pass
    else:
        print('PASSWORD SHOULD CONTAIN special chracters and numbers')   
        
password_collector() 
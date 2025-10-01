import re
import string

password = input('Entre your password:')

if len(password) >= 8:
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)   
    has_digit = any(c.isdigit() for c in password) 
    has_special = any(c  in string.punctuation for c in password)
    if has_upper and has_upper and has_digit and has_special:
        print(f'Your password {password} is STRONG , it has at least 8 characeters with both uppercase and lowercase and also numbers and special characeters.')
    else:
        if not has_upper or has_lower:
            print('Your password should have both uppercase and lowercase letter.')
        if not has_digit or has_special:
            print('Your password should have numbers and special characeters.')
else: 
    print('Password length should be at least 8 characeters.')
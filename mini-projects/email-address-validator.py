def email_address_validator(email):
    dot = email.rfind('.')
    at = email.rfind('@')
    if dot == -1 or at == -1: 
        return False
    if dot < at: 
        return False
    if dot == len(email) - 1 or at == len(email) - 1: 
        return False
    if dot == 0 or at == 0: 
        return False
    if email.count('@') != 1:
        return False
    return True

while True:
    email = input('Enter the email address: ')
    if email_address_validator(email):
        print('Valid email address.')
    else:
        print('Invalid email address.')



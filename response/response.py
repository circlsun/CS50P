from validator_collection import validators, checkers, errors


is_email_address = checkers.is_email(input("What's your email address? "))
if is_email_address:
    print('Valid')
else:
    print('Invalid')

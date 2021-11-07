"""
Rewrite the function. which you already have password_validate so that an exception is thrown if the password is invalid
"""


def validate_password(password):
    if len(password) <= 8:
        raise ValueError
    for i in password:
        if 'A' <= i <= 'Z':
            return True
    raise ValueError


print('validane_password', validate_password("jkkkjjjjjg"))

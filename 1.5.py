# An integer is entered to indicate the ASCII character code. Determine if this is an English letter code or some other symbol.

v = int(input('Enter code in DEC >>> '))
if 65 <= v <= 90 or 97 <= v <= 122:
    print('Latin letters of different registers')
else:
    print('other')

# An integer is entered to indicate the ASCII character code. Determine if this is an English letter code or some other symbol.

v = int(input('Enter code in DEC >>> '))
if 101 <= v <= 132 or 141 <= v <= 172:
    print('Latin letters of different registers')
else:
    print('other')

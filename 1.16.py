# The user enters the year. Determine whether it is high-axle or not.

year = int(input('Enter year'))
if year % 4 == 0:
    print('High-axel')
else:
    print('None')

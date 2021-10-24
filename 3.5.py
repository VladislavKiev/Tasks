"""
5) The user enters the number of the month, the function returns the time of year.
"""


def year():
    seasons = { 'Winter': (1, 2, 12),
                'Spring': (3, 4, 5),
                'Summer': (6, 7, 8),
                'Autumn': (9, 10, 11)}

    month = int(input('Enter the number of the month >>> '))
    for key in seasons.keys():
        if month in seasons[key]:
            print(key)
            break
    else:
        print('Enter correct number')


year()

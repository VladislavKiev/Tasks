# Two squares of a chessboard are given. If they are colored in the same color, then print the word YES, and if they are in different colors - then NO. The program receives as input four numbers from 1 to 8 each, specifying the column number and line number, first for the first cell, then for the second cell.

a = int(input('Enter first row>>>> '))
b = int(input('Enter first column>>>> '))
c = int(input('Enter second row>>>> '))
d = int(input('Enter second column>>>> '))
e = int(a * b % 2 == 0)
f = int(c * d % 2 == 0)
if a and b and c and d in range(1, 9):
    if e == 0:
        print('the first color is black')
    else:
        print('the first color is white')
    if f == 0:
        print('the second color is black')
    else:
        print('the second color is white')
    if e == f:
        print('Yes')
    else:
        print('No')
else:
    print('Enter correct value')


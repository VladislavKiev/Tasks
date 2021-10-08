# If a temperature is entered in degrees Celsius, it is converted to a temperature in Fahrenheit. Or vice versa: Fahrenheit temperature is converted to Celsius temperature.

a = input('Enter the temperature, the last character should be C or F >>> ')
temp = float(a[:-1])
if a[-1] == 'F':
    c = (temp-32)*5/9
    print(c, 'C')
elif a[-1] == 'C':
    f = temp*9/5 + 32
    print(f, 'F')
else:
    print('Enter correct value')

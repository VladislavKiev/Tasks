# The user makes a deposit in the amount of N $ for a period of years at 11.5% per annum (each year the size of his deposit increases by 11.5%. This money is added to the amount of the deposit, and next year there will also be interest on them). Write a program where the user enters the arguments a and years, and calculate the amount that will be on the user's account after years.

am = float(input('Enter amount >>>'))
years = int(input('Enter the term in years>>> '))
dep = 0.115
for i in range(1, years + 1):
    am = am + am*dep
print('The result would be ', am)

# The factorial of the number n is the number 𝑛! = 1 ∙ 2 ∙ 3∙… ∙ 𝑛. Create a program that calculates the factorial of a user-entered number. (Cycle!)

a = int(input('Enter value >>> '))
res = 1
for i in range(1, a+1):
    res = i * res
    print(res)
print(res)



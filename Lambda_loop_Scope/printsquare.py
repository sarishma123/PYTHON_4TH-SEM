def Myfunction(n):
    return lambda x: x * x

a = int(input("Enter the number: "))
mysquare = Myfunction(a)
print(mysquare(a))

# for odd and even 
def Odd_even(n):
    return lambda x: x % 2 == 0

a = int(input("Enter the number: "))
Check = Odd_even(a)
print(Check(a))
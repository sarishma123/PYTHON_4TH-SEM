# to print the square root of the number
def squareroot():
    a = int(input("Enter the number: "))
    b = a ** (1/2)
    print("The square root of the number is:", b)

squareroot()

# Terminal-based calculator

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def divi(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

def calculator():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    print("Choose an operation:\n")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Division")

    ch = input("Enter your choice (1-4): ")

    match ch:
        case "1":
            print("Result of the addiotn is :", add(a, b))
        case "2":
            print("Result of the subtraction is :", sub(a, b))
        case "3":
            print("Result of the multiply is :", mul(a, b))
        case "4":
            print("Result is the division is :", divi(a, b))
        case _:
            print("Invalid choice!")

calculator()


# to check the greatest number between 3 numbers:

# To check the greatest number among three numbers

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

print("The numbers you entered are:")
print("a =", a)
print("b =", b)
print("c =", c)

if a >= b and a >= c:
    print("a is the greatest:", a)
elif b >= a and b >= c:
    print("b is the greatest:", b)
else:
    print("c is the greatest:", c)



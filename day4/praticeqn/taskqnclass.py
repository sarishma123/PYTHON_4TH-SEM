def find_average(*args):
    total = 0
    for num in args:
        total += num
    average = total / len(args)
    print("Average =", average)

find_average(10, 20, 30, 40, 50)

# to seprate the odd and even numbers

def Odd_or_Even(*args):
    odd=0
    even=0
    for num in args:
        if num %2==0:
            print("even",num)
        else:
            print("odd",num)
Odd_or_Even(2,10,40,55,57,99,101,100,250,222,1,0)

# functional program that accept certains things
def Employee(*args):
    print("Name:", args[0])
    print("Salary:", args[1] + args[2])
    print("Department:", args[3])
    print("Experience:", args[4], "years")

Employee("Ram", 50000, 60000, "IT", 3)

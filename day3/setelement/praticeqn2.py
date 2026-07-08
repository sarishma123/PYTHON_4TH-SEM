# Create a tuple of 5 numbers
numbers = (10, 20, 30, 40, 50)
total = sum(numbers)
average = total / len(numbers)
print("Tuple:", numbers)
print("Sum:", total)
print("Average:", average)

# to print the last three elemetns using slicing
print("All numbers:", numbers[:])
print("last three numbers:", numbers[-3:])

# given the tuple of string.return the longest string
string=("sarishma", "ram","shyam","sita")
longest = ()
longest=max(string, key=len)
print("the longest one is ", longest)


# to merge the tuple
a=(9,7,5,6,4,5,61)
b=(4,5,343,44,22,33)
c=a+b
print("Sorted merged tuple:", c)

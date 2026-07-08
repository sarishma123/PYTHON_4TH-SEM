# To make the set of even numbers from 1 to 20
even = {x for x in range(1, 21) if x % 2 == 0}
print("1. Even numbers:", even)

# Ask the user to input a number and check whether it exists
a = int(input("Enter the number to check: "))

if a in even:
    print("The number is there.")
else:
    print("The number is not there.")

# Remove duplicate elements
nums = [1, 2, 2, 3, 4, 2, 4, 53, 2, 34, 3, 3, 2]

newset= set(nums)

print("Original list:", nums)
print("After removing duplicates:",newset)

# to print and even set of uinion intersextion and difference

# Lists
new = [1, 2, 3, 3, 4, 5, 65, 4]
nums = [1, 2, 2, 3, 4, 2, 4, 53, 2, 34, 3, 3, 2]

# Convert lists to sets
set1 = set(new)
set2 = set(nums)

print("Set 1:", set1)
print("Set 2:", set2)

# Union
print("Union:", set1.union(set2))


# Intersection
print("Intersection:", set1.intersection(set2))
# or
print("Intersection:", set1 & set2)

# Difference
print("Difference (set1 - set2):", set1.difference(set2))

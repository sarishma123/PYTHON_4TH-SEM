
# QUESTION 1: Count frequency of each character
#             in a string (excluding spaces)
# -----------------------------------------------

print("=" * 40)
print("QUESTION 1: Character Frequency")
print("=" * 40)

my_string = input("Enter a string: ")

frequency = {}  # empty dictionary to store counts

for char in my_string:
    if char != " ":  # skip spaces
        if char in frequency:
            frequency[char] += 1   # already seen, add 1
        else:
            frequency[char] = 1    # first time seeing it

print("Character frequencies:")
for char, count in frequency.items():
    print(f"  '{char}' -> {count}")



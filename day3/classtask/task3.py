
# -----------------------------------------------
# QUESTION 3: Group words by their starting letter
# -----------------------------------------------

print("\n" + "=" * 40)
print("QUESTION 3: Group Words by Starting Letter")
print("=" * 40)

words = ["apple", "banana", "avocado", "blueberry", "cherry", "apricot", "cranberry"]

print("Words:", words)

grouped = {}  # dictionary to hold groups

for word in words:
    first_letter = word[0]  # get the first letter

    if first_letter in grouped:
        grouped[first_letter].append(word)   # add to existing list
    else:
        grouped[first_letter] = [word]        # start a new list

print("Grouped by starting letter:")
for letter, word_list in grouped.items():
    print(f"  '{letter}' -> {word_list}")


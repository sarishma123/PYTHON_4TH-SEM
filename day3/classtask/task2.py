# -----------------------------------------------
# QUESTION 2: Student names and marks
#             Find student(s) with highest marks
# -----------------------------------------------

print("\n" + "=" * 40)
print("QUESTION 2: Highest Scoring Student(s)")
print("=" * 40)

students = {
    "Alice": 85,
    "Bob":   92,
    "Carol": 78,
    "David": 92,
    "Eve":   88
}

print("Student marks:", students)

highest_marks = max(students.values())  # find the highest mark

top_students = []
for name, marks in students.items():
    if marks == highest_marks:
        top_students.append(name)  # collect all who got highest

print(f"Highest marks: {highest_marks}")
print(f"Top student(s): {top_students}")


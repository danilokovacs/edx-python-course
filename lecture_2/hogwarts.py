students = ["Hermione", "Harry", "Ron"]

for name in students:
    print(f"Student name: {name}")

print(f"Ranking students")
for i in range(len(students)):
    print(i + 1, students[i], i, students[i])
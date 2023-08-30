"""
######### Problem 1.1
#same problem as above, but output should have the student name and all the marks in the same line.
# Eg - Input - Student Name - Chitra, Mark1 1 55, Mark 2 67
#output -  Chitra's marks 55, 67
"""
for student in range(1, 4):
    student_name = input(f"Enter name of student {student}: ")
    marks = []
    for mark in range(1, 3):
        input_mark = float(input(f"Enter mark {mark} for {student_name}: "))
        marks.append(input_mark)
    print(f"{student_name}'s marks {marks[0]}, {marks[1]}")

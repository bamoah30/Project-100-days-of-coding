student_heights = input("Please enter a list of students' heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n]=int(student_heights[n])
print(f"These are the heights you entered: {student_heights}")
total_heights = 0
number_of_students = 0
for height in student_heights:
    total_heights += height
    number_of_students += 1
print(f"The average of the heights is {round(total_heights/number_of_students)}")

student_scores = input("Please enter a list of students' scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n]=int(student_scores[n])
print(f"These are scores you entered: {student_scores}")
max_score = 0
for score in student_scores:

    if score >= max_score:
        max_score = score
        continue

print(f"The highest score is {max_score}")
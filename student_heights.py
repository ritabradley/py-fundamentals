student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
	student_heights[n] = int(student_heights[n])

num_students = 0
count = 0

for height in student_heights:
	num_students += 1
	count += height

avg = round(count / num_students)
print(avg)

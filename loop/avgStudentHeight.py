student_heights = [165, 166, 178, 157, 152, 173, 180]
total_height = 0
total_number_of_students = 0 

for height in student_heights:
    total_height =  total_height + height
    total_number_of_students += 1

avg_height = total_height // total_number_of_students

print(avg_height)
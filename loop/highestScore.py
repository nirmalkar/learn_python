student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
# print(max(student_scores))
# print(min(student_scores))
current_highest_score = student_scores[0]
current_lowest_score = student_scores[0]
for score in student_scores:
    if (score > current_highest_score):
        current_highest_score = score
    if(score < current_lowest_score):
        current_lowest_score = score

print(f'The highest score is {current_highest_score}')
print(f'The lowest score is {current_lowest_score}')
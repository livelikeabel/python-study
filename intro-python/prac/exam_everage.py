kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 50, 90]
eng_score = [49, 79, 48, 60, 100]
midterm_score = [kor_score, math_score, eng_score]

student_score = [0, 0, 0, 0, 0]
for subject in midterm_score:
    i = 0
    for score in subject:
        student_score[i] += score
        i += 1
else:
    a, b, c, d, e = student_score
    student_everage = [a/3, b/3, c/3, d/3, e/3]
    print(student_everage)
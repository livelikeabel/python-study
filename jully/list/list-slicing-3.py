scores = list()
n = int(input("학생의 수: "))

for i in range(n):
    score = input("{}번째 학생 3과목 점수:".format(i + 1)).split(' ')
    scores.append(score)

print(scores)


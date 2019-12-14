score = [
    [90, 40, 30, 50, 60, 40, 60, 40],
    [20, 30, 40, 50, 30, 20, 60, 40],
    [10, 30, 40, 30, 20, 50, 60, 40]
]

for i in range(3):
    min = score[i][0]
    for j in range(8):
        if score[i][j] < min:
            min = score[i][j]
    print("Min[{}]={}".format(i, min))
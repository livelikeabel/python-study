mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def solution(mylist):
    answer = [[]]
    for n in range(len(mylist) - 1):
        answer.append([])

    for i, v in enumerate(mylist):
        for j, w in enumerate(v):
            answer[i].append(mylist[j][i])
            print(answer)

    return answer


solution(mylist)

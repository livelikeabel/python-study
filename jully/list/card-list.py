# 3명의 카드 숫자를 저장해놓는 리스트 p가 있다. 변수 n에 숫자를 입력받고, n번동안 3명의 사람이 새롭게 카드를 뽑는다.
# 이 때, 새로 뽑은 카드가 기존에 뽑은 카드보다 높으면 p에 카드 숫자를 새로 뽑은 카드로 변경한다.
# n번 반복 후 가장 높은 카드 숫자를 가진 사람이 승리하며 번호를 출력한다. (단, 동점이 있을 경우 앞사람이 승리한다.)

# 2
# Person1 Card = 4
# Person2 Card = 8
# Person3 Card = 6
# [4, 8, 6]
# Person1 Card = 5
# Person2 Card = 7
# Person3 Card = 9
# [5, 8, 9]
# Person3 Win

p = [0, 0, 0]
n = int(input())

for i in range(n):
    for j in range(3):
        card = int(input("Person %i Card =" % (j + 1)))
        if p[j] < card:
            p[j] = card
    print(p)

max_num = max(p)
player = p.index(max_num) + 1

print('Person %i Win' % player)

import random

random_num = random.randint(1, 100)
user_num = int(input())

while user_num is not random_num:
    if user_num < random_num:
        print('좀 더 높게 ㄱㄱ')
    if user_num > random_num:
        print('좀 더 낮게 ㄱㄱ')
    user_num = int(input())

print('정답!')
x = 1

while(x is not 0):
    x = int(input())
    if x == 0: break
    if not(1 <= x <= 9):
        print('잘못 입력하셨습니다. 1부터 9사이의 수를 입력해 주세요 :)')
        continue
    else:
        for i in range(1,10):
            print(x, '*', i, '=', x*i)

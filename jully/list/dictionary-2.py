user_info = {'name': 'David', 'age': 21, 'address': '서울시 광진구'}
key = input("원하는 정보:")

if key in user_info:
    print(key, ':', user_info[key])

else:
    print('해당되는 정보가 존재하지 않습니다.')

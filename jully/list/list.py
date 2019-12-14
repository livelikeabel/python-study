import random

rooms = [0 for i in range(10)]

for room in rooms:
    idx = random.randint(0, 9)
    num = random.randint(1, 10)
    rooms[idx] = num

total = 0
for room in rooms:
    if room > 5:
        total += 1

print(rooms)
print(total)
score = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]

for v in score:
    print('Min[{}] = {}'.format(score.index(v), min(v)))
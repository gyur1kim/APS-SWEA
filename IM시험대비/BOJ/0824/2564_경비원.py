import sys
sys.stdin = open('2564.txt')

width, height = map(int, input().split())
# street = [[0]*width for _ in range(height)]
storesN = int(input())
stores = [list(map(int, input().split())) for _ in range(storesN)]
donggune = list(map(int, input().split()))

'''
1 : 북쪽
2 : 남쪽  -> 2번째 값은 왼쪽으로부터의 거리
3 : 서쪽
4 : 동쪽  -> 2번째 값은 위쪽으로부터의 거리

좌표로 관리하면 좋지 않을까용??
'''
# 동근이의 행,렬 구하기
if donggune[0] == 1:
    dongguneI = 0
    dongguneJ = donggune[1]
elif donggune[0] == 2:
    dongguneI = height-1
    dongguneJ = donggune[1]
elif donggune[0] == 3:
    dongguneI = donggune[1]
    dongguneJ = 0
else:
    dongguneI = width-1
    dongguneJ = donggune[1]

print(street)

for cardinalPoint, far in stores:    # 방위, 얼마나 떨어져있는지...
    if cardinalPoint == 1:
        storeI = 0
        storeJ = far

    elif cardinalPoint == 2:
        storeI = height - 1
        storeJ = far
    elif cardinalPoint == 3:
        storeI = far
        storeJ = 0
    else:
        storeI = width - 1
        storeJ = far


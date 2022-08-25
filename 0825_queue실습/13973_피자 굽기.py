import sys
sys.stdin = open('13973.txt')
from collections import deque


T = int(input())
for tc in range(1, T+1):
    ovenSize, pizzaNum = map(int, input().split())   # 화덕 크기와 구울 피자 갯수
    pizzas = list(map(int, input().split()))
    bakingNow = deque()

    inOven = 0
    for i, pizza in enumerate(pizzas, 1):
        if i > ovenSize:
            break
        bakingNow.append((i, pizza))
        inOven = i

    while bakingNow:
        num, leftCheese = bakingNow.popleft()
        leftCheese = leftCheese // 2
        if leftCheese == 0:
            if inOven < pizzaNum:
                inOven += 1
                bakingNow.append((inOven, pizzas[inOven - 1]))
        else:
            bakingNow.append((num, leftCheese))

    print(f'#{tc} {num}')
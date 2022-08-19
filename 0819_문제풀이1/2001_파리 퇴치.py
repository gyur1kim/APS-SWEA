import sys
sys.stdin = open('2001.txt')

T = int(input())
for tc in range(1, T+1):
    arrSize, flyswatterSize = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(arrSize)]

    maxFlies = 0
    for i in range(arrSize - flyswatterSize + 1):
        for j in range(arrSize - flyswatterSize + 1):
            flies = 0
            for s1 in range(flyswatterSize):
                for s2 in range(flyswatterSize):
                    flies += arr[i + s1][j + s2]
            if maxFlies < flies:
                maxFlies = flies
    print(f'#{tc} {maxFlies}')
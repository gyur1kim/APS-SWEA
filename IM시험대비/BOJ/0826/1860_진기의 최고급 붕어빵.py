import sys
sys.stdin = open('1860.txt')

T = int(input())
for tc in range(1, T+1):
    personN, secM, K = map(int, input().split())  # 사람 수 N, 붕어빵 만드는 시간 M, 붕어빵 K개
    personSec = list(map(int, input().split()))   # 각 사람들이 오는 시간.
    personSec.sort()
    round = 1
    while personSec:
        if personSec[0] < secM * round:
            print(f'#{tc} Impossible')
            break
        personSec = personSec[K:]
        round += 1
    if not personSec:
        print(f'#{tc} Possible')
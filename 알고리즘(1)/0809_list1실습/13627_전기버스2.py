import sys
sys.stdin = open('13627.txt')

T = int(input())
for tc in range(1, T+1):
    maxDist, end, chargeNum = map(int, input().split())
    chargingStation = [0] + list(map(int, input().split())) + [end]
    # 0 4 7 9 14 17 20, 5씩 감
    now = cnt = 0
    for i in range(1, chargeNum+2):
        if chargingStation[i] - chargingStation[i-1] > maxDist:
            cnt = 0
            break
        elif chargingStation[i] - chargingStation[now] > maxDist:
            now = i-1
            cnt += 1
    print(f'#{tc} {cnt}')
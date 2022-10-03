import sys
sys.stdin = open('6485.txt')

T = int(input())
for tc in range(1, T+1):
    busStops = [0] * 5001
    buses = int(input())
    busGoesTo = [list(map(int, input().split())) for _ in range(buses)]
    ans = ''
    for i in range(buses):
        for stop in range(busGoesTo[i][0], busGoesTo[i][1] + 1):
            busStops[stop] += 1

    P = int(input())
    for _ in range(P):
        station = int(input())
        ans += str(busStops[station]) + ' '
    print(f'#{tc} {ans}')
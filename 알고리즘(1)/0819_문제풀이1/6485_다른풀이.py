import sys
sys.stdin = open('6485.txt')

T = int(input())
for tc in range(1, T+1):
    buses = int(input())
    busFromTo = [list(map(int, input().split())) for _ in range(buses)]
    ans = ''
    P = int(input())
    for _ in range(P):
        station = int(input())
        cnt = 0
        for fromTo in busFromTo:
            if fromTo[0] <= station <= fromTo[1]:
                cnt += 1
        ans += str(cnt) + ' '
    print(f'#{tc} {ans}')
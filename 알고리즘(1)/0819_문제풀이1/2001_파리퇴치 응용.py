import sys
sys.stdin = open('2001_파리퇴치_대각선.txt')
# 파리채가 X자인.. 그런 희안한 경우를 만들어보자,,,

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())      # N: 배열 크기, M: 파리채 크기
    arr = [list(map(int, input().split())) for _ in range(N)]

    maxFlies = -99
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            sumFlies = 0
            for num in range(M):
                sumFlies += arr[i+num][j+num]
                sumFlies += arr[i+num][j + M - 1 - num]
                if num == M//2:          # 대각선의 가운데 중복되는거 빼기
                    sumFlies -= arr[i+num][j+num]
            if sumFlies > maxFlies:
                maxFlies = sumFlies
    print(f'#{tc} {maxFlies}')
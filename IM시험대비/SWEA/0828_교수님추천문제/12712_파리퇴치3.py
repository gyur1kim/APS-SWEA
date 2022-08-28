import sys
sys.stdin = open('12712.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())   # N은 배열 크기, M은 파리채 크기

    arr = [[0] * (N+(M-1)*2) for _ in range(M-1)]
    arr.extend([[0]*(M-1) + list(map(int, input().split())) + [0]*(M-1) for _ in range(N)])
    arr += [[0] * (N+(M-1)*2) for _ in range(M-1)]

    maxFlies = 0
    for i in range(M-1, N+M-1):
        for j in range(M-1, N+M-1):
            # +모양으로 잡기!!
            flies = -arr[i][j]
            for k in range(-M+1, M):
                flies += arr[i+k][j]
                flies += arr[i][j+k]
            maxFlies = flies if flies > maxFlies else maxFlies

            # X자로 잡기
            flies = -arr[i][j]
            for k in range(-M+1, M):   # -2 -1 0 1 2
                flies += arr[i+k][j+k]
                flies += arr[i+k][j-k]
            maxFlies = flies if flies > maxFlies else maxFlies
    print(f'#{tc} {maxFlies}')

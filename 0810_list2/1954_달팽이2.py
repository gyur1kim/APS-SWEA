import sys
sys.stdin = open('1954.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    i = j = 0
    arr[i][j] = 1
    n = 2
    while n <= N**2:
        while j+1 < N and arr[i][j+1] == 0:
            j += 1
            arr[i][j] = n
            n += 1
        while i+1<N and arr[i+1][j] == 0:
            i += 1
            arr[i][j] = n
            n += 1
        while j-1 >= 0 and arr[i][j-1] == 0:
            j -= 1
            arr[i][j] = n
            n += 1
        while i-1 >= 0 and arr[i-1][j] == 0:
            i -= 1
            arr[i][j] = n
            n += 1
    print(f'# {t}')
    for a in arr:
        print(*a)
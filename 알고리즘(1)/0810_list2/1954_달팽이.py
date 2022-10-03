import sys
sys.stdin = open('1954.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    i = j = turn = 0

    for n in range(1, N**2+1):
        arr[i][j] = n

        #이런 누더기 코드도 받아주나여?ㅜ
        if i == 0+turn:
            if j == N-1-turn:
                i += 1
            else:
                j += 1
        elif j == N-1-turn:
            if i == N-1-turn:
                j -= 1
            else:
                i += 1
        elif i == N-1-turn:
            if j == 0+turn:
                i -= 1
            else:
                j -= 1
        elif j == 0+turn:
            if i == 0+turn:
                j += 1
            elif i == 0+turn+1:
                turn += 1
                j += 1
            else:
                i -= 1




    print(f'#{t}')
    for a in arr:
        print(*a)
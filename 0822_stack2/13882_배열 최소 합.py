import sys
sys.stdin = open('13882.txt')


def sumMin(N, res, acc, row):  # N: 배열 크기, res: idx담을 배열, acc: 값의 누적, row:현재 행
    global minimum
    if row == N:
        if minimum > acc:
            minimum = acc
        return

    for i in range(N):
        if i not in res:
            if acc + arr[row][i] >= minimum:
                continue
            res.append(i)
            sumMin(N, res, acc + arr[row][i], row+1)
            res.pop()
    return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    if tc != 3:
        continue

    res = []
    minimum = N * 9 + 1
    sumMin(N, res, 0, 0)
    print(f'#{tc} {minimum}')
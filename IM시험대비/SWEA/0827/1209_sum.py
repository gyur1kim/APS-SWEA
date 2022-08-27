import sys
sys.stdin = open('1209.txt')

for _ in range(1, 11):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    resMax = 0

    # 가로세로대각선 더하기
    diagonalFromLeft = 0
    diagonalFromRight = 0
    for i in range(100):
        diagonalFromLeft += arr[i][i]
        diagonalFromRight += arr[i][99 - i]
        row = 0
        col = 0
        for j in range(100):
            row += arr[i][j]
            col += arr[j][i]
        if max(row, col) > resMax:
            resMax = max(row, col)
    if max(diagonalFromRight, diagonalFromLeft) > resMax:
        resMax = max(diagonalFromRight, diagonalFromLeft)

    print(f'#{t} {resMax}')
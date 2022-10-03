import sys
sys.stdin = open('13924.txt')


def escapeMaze():
    pass


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    nextX = [-1, 0, 1, 0]
    nextY = [0, 1, 0, -1]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                startX = i
                startY = j


    print(f'#{tc} ')
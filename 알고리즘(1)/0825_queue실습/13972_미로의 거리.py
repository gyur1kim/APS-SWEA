import sys
sys.stdin = open('13972.txt')
from collections import deque


def mazeBFS(i, j, N):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = 1

    while queue:
        # print(visited)
        i, j = queue.popleft()
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni = i + di
            nj = j + dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                if maze[ni][nj] == 2:
                    return visited[i][j] - 1
                queue.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    startI = startJ = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 3:
                startI, startJ = i, j
                break
    # print(maze)
    print(f'#{tc} {mazeBFS(startI, startJ, N)}')
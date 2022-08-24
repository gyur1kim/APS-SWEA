import sys
sys.stdin = open('1226.txt')


def bfs(i, j):
    visited = [[0]*16 for _ in range(16)]
    queue = []
    queue.append((i, j))
    visited[i][j] = 1
    while queue:
        i, j = queue.pop(0)
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nx = i + di
            ny = j + dj
            if nx == 13 and ny == 13:
                return 1
            if maze[nx][ny] != 1 and visited[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = visited[i][j] + 1
    return 0

for _ in range(1, 11):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    print(f'#{tc} {bfs(1, 1)}')

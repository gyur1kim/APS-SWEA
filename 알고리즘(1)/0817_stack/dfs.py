adjList = [[1, 2],
           [0, 3, 4],
           [0, 4],
           [1, 5],
           [1, 2, 5],
           [3, 4, 6],
           [5]]


def dfs(v, N):
    visited = [0] * N
    stack = [0] * N
    top = -1
    print(v)

    visited[v] = 1
    while True:
        for w in adjList[v]:
            if visited[w] == 0:
                top += 1
                stack[top] = v
                visited[w] = 1
                v = w
                print(v)
                break
        else:
            if top != -1:
                v = stack[top]
                top -= 1
            else:
                break


dfs(0, 7)
print()
dfs(1, 7)
print()
dfs(2, 7)
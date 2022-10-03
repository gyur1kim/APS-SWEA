'''
0번부터 V번까지, E개의 간선
6 8
0 1
0 2
1 3
1 4
2 4
3 5
4 5
5 6
'''


def BFS(v, N):  # 그래프 G, v: 시작 정점, N: 노드 갯수
    # visited 생성
    visited = [0] * (N+1)
    # 큐 생성
    queue = []
    # 시작점 인큐
    queue.append(v)
    # 시작점 처리 표시
    visited[v] = 1

    # 큐가 비어있지 않으면!
    while queue:
        # 지금 온 곳을 꺼내자
        v = queue.pop(0)
        print(v)
        # 방문한 곳 처리하기
        # 인접하고 미방문(enqueue안했음)한 정점 w가 있으면
        for w in adjList[v]:
            if visited[w] == 0:
                queue.append(w)
                visited[w] = visited[v]+1


V, E = map(int, input().split())
N = V + 1
adjList = [[] for _ in range(N)]
visited = [0] * N
for _ in range(E):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)

BFS(0, N)
import sys
sys.stdin = open('13974.txt')


def bfs(start, arrive, V):
    queue = [start]
    visited = [0]*(V+1)
    visited[start] = 1
    while queue:
        fromNode = queue.pop(0)
        for i in nodeDict.get(fromNode, [-1]):
            if i == -1:
                break
            if visited[i] == 0:
                if i == arrive:
                    return visited[fromNode]
                queue.append(i)
                visited[i] = visited[fromNode] + 1
    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())   # V: 노드의 개수, E: 간선의 개수
    nodeDict = {}
    for _ in range(E):
        go, to = map(int, input().split())
        v = nodeDict.get(go, [])
        v.append(to)
        nodeDict[go] = v
        v = nodeDict.get(to, [])
        v.append(go)
        nodeDict[to] = v
    S, G = map(int, input().split())   # S: 시작 노드, G: 도착 노드

    print(f'#{tc} {bfs(S, G, V)}')

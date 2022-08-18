import sys
sys.stdin = open('13808.txt')


def dfs(currentNode, endNode):
    global nodeDict, visited
    visited.add(currentNode)
    if nodeDict.get(currentNode):
        for n in nodeDict.get(currentNode):
            if n == endNode:
                return 1
            if n not in visited:
                if dfs(n, endNode):
                    return 1


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    nodeDict = {}
    visited = set()
    for _ in range(E):
        fromNode, toNode = map(int, input().split())
        v = nodeDict.get(fromNode, [])
        v.append(toNode)
        nodeDict[fromNode] = v
    print(nodeDict)
    start, end = map(int, input().split())
    print(f'#{tc} {1 if dfs(start, end) else 0}')

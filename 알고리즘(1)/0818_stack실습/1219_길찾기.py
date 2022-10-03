import sys
sys.stdin = open('1219.txt')


def dfs(currentNode):
    global nodeDict, visited
    visited.add(currentNode)
    # stack = [currentNode]
    if nodeDict.get(currentNode):
        for n in nodeDict.get(currentNode):
            # print(f'currentNode : {currentNode}, n : {n}')
            if n == 99:
                return 1
            if n not in visited:
                # res = dfs(n)
                if dfs(n):
                    return 1


    # visited = set()
    # visited.add(currentNode)
    #
    # while True:
    #     if nodeDict.get(currentNode):
    #         for n in nodeDict.get(currentNode):
    #             if n == 99:
    #                 return 1
    #             elif n not in visited:
    #                 stack.append(n)
    #                 visited.add(n)
    #                 currentNode = n
    #                 break
    #         else:
    #             if len(stack) > 2:
    #                 stack.pop()
    #                 currentNode = stack[-1]
    #             else:
    #                 return 0
    #     else:
    #         if len(stack) > 2:
    #             stack.pop()
    #             currentNode = stack[-1]
    #         else:
    #             return 0


for _ in range(10):
    tc, E = map(int, input().split())
    nodes = list(map(int, input().split()))
    visited = set()
    nodeDict = {}
    for e in range(E):
        node1, node2 = nodes[e*2:(e+1)*2]
        lst = nodeDict.get(node1, [])
        lst.append(node2)
        nodeDict[node1] = lst
    print(nodeDict)
    print(f'#{tc} {1 if dfs(0) else 0}')
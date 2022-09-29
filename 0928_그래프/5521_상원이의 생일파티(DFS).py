import sys
sys.stdin = open('5521.txt')

# 제출했는데 틀린 코드 ㄱ-
'''
def DFS(friend, depth):
    global invited

    for f in friends.get(friend, []):
        if f == 1:
            continue
        invited.add(f)
        if depth+1 <= 2:
            DFS(f, depth+1)


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())  #N: 반의 사람 수, M: 친한 친구 수
    friends = {}
    invited = set()

    # 딕셔너리에 넣기~
    for _ in range(M):
        a, b = map(int, input().split())
        friends[a] = friends.get(a, [])
        friends[a].append(b)
    DFS(1, 1)

    print(f'#{tc} {len(invited)}')
'''

# 인접 행렬
# 교수님 코드인데..이것도 안되는데??ㅜㅜㅜㅜ
'''
def dfs(i, N, c):
    if c == 3:
        return
    else:
        visited[i] = 1
        for j in range(1, N+1):
            if adjM[i][j] and visited[j] == 0:
                dfs(j, N, c+1)


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())  #N: 반의 사람 수, M: 친한 친구 수
    adjM = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        adjM[a][b] = 1
        adjM[b][a] = 1
    visited = [0] * (N+1)
    dfs(1, N, 0)

    print(f'#{tc} {sum(visited)-1}')
'''
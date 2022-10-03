def permutation(row, sum, depth):
    global min_v
    if depth == N:
        if sum < min_v:
            min_v = sum
        return

    for i in range(N):  # i가 열이라구
        if visited[i]:
            continue

        if sum + arr[row][i] > min_v:
            continue
        visited[i] = True
        permutation(row+1, sum + arr[row][i], depth+1)
        visited[i] = False


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    min_v = N * 10
    permutation(0, 0, 0)
    print(f'#{tc} {min_v}')
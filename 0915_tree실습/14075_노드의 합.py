import sys
sys.stdin = open('14075.txt')


def preorder(n):
    if n*2 < N:
        left = preorder(n*2)
        right = preorder(n*2+1)
        tree[n] = left + right
    elif n*2 == N:
        tree[n] = tree[n*2]
    return tree[n]


T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    # 트리 리프 부분 만들기
    for _ in range(M):
        i, v = map(int, input().split())
        tree[i] = v

    # 어이어이 후위순회냐구 이거~
    print(f'#{tc} {preorder(L)}')
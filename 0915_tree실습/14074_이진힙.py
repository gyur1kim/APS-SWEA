import sys
sys.stdin = open('14074.txt')
'''
이진 최소힙 : 부모가 제일 작고 자식이 제일 커야된다...!!!
우엥
'''
T = int(input())
for tc in range(1, T+1):
    V = int(input())
    heap = [0] + list(map(int, input().split()))
    for i in range(2, V+1):
        c = i
        p = i//2
        while p and heap[c] < heap[p]:
            heap[c], heap[p] = heap[p], heap[c]
            c = p
            p = c//2
    p = V//2
    res = 0
    while p:
        res += heap[p]
        p = p//2
    print(f'#{tc} {res}')
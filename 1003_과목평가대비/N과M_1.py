import sys
sys.stdin = open('N과M_1.txt')

def permutation(depth):
    if depth == b:
        print(*lst)

    for i in range(1, a+1):
        if i not in lst:
            lst.append(i)
            permutation(depth+1)
            lst.pop()


a, b = map(int, input().split())
lst = []
permutation(0)



import sys
sys.stdin = open('1231.txt')

def inorder(a):
    if a <= E:
        inorder(2 * a)
        print(par[a], end='')
        inorder(2 * a + 1)

for tc in range(1, 11):
    E = int(input())
    # par 자식인덱스에 부모번호 저장 할 리스트
    par = [0] * (E + 1)
    root = 1

    for i in range(E):
        lst = list(input().split())
        par[i+1] = lst[1]
    print(f'#{tc} ', end='')
    inorder(root)
    print()
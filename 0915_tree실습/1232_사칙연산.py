import sys
sys.stdin = open('1232.txt')


def tree(v):
    if type(val[v]) == str:
        a = tree(ch1[v])
        b = tree(ch2[v])
        if val[v] == '-':
            return a - b
        elif val[v] == '+':
            return a + b
        elif val[v] == '*':
            return a * b
        elif val[v] == '/':
            return a / b
    else:
        return val[v]


for tc in range(1, 11):
    V = int(input())
    val = [0] * (V+1)
    ch1 = [0] * (V+1)
    ch2 = [0] * (V+1)
    root = 1

    for i in range(V):
        n, *tmp = list(input().split())
        # print(tmp)
        if len(tmp) != 1:
            val[int(n)] = tmp[0]
            ch1[int(n)] = int(tmp[1])
            ch2[int(n)] = int(tmp[2])
        else:
            val[int(n)] = int(tmp[0])
    print(f'#{tc} {int(tree(root))}')
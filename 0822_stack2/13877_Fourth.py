import sys
sys.stdin = open('13877.txt')

def forth(postfix):
    numStack = []
    for n in postfix:
        if n == '.':
            if len(numStack) > 1:
                return 'error'
            return numStack.pop()
        if n.isdigit():
            numStack.append(int(n))
        else:
            if len(numStack) < 2:
                return 'error'
            a = numStack.pop()
            b = numStack.pop()
            if n == '+':
                numStack.append(b+a)
            elif n == '-':
                numStack.append(b-a)
            elif n == '/':
                numStack.append(int(b/a))
            elif n == '*':
                numStack.append(b*a)


T = int(input())
for tc in range(1, T+1):
    postfix = input().split()
    print(f'#{tc} {(forth(postfix))}')
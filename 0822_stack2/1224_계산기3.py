import sys
sys.stdin = open('1224.txt')

def toPostfix(exp):
    isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}  # 스택에 들어있을 때 우선순위
    icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3}  # 스택에 들어올 때 우선순위

    postfix = ''
    tokenStack = []
    for e in exp:
        if e.isdigit():
            postfix += e
        else:
            if len(tokenStack) == 0:
                tokenStack.append(e)
            elif e == ')':
                while tokenStack[-1] != '(':
                    postfix += tokenStack.pop()
                tokenStack.pop()
            else:
                while len(tokenStack) > 0 and icp[e] < isp[tokenStack[-1]]:
                    postfix += tokenStack.pop()
                tokenStack.append(e)
    postfix += ''.join(reversed(tokenStack))
    return postfix


def calculate(postfix):
    numStack = []
    for n in postfix:
        if n.isdigit():
            numStack.append(int(n))
        else:
            a = numStack.pop()
            b = numStack.pop()
            if n == '+':
                numStack.append(b + a)
            elif n == '-':
                numStack.append(b - a)
            elif n == '/':
                numStack.append(int(b / a))
            elif n == '*':
                numStack.append(b * a)
    return numStack.pop()


for tc in range(1, 11):
    n = int(input())
    expression = input()

    print(f'#{tc} {calculate(toPostfix(expression))}')

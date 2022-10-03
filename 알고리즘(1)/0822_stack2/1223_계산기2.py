import sys
sys.stdin = open('1223.txt')
'''
스택에 넣을 때 나보다 우선순위가 낮으면 넣어버림
들어있는게 나보다 우선순위가 높으면, 낮은게 나올 떄까지 pop
'''

for tc in range(1, 11):
    n = int(input())
    expression = input()

    postfix = ''
    postfixStack = []
    for x in expression:
        if x.isdigit():          # 숫자면 출력
            postfix += x
        else:
            if x == '+':
                while len(postfixStack) > 0 and postfixStack[-1] == '*':
                    postfix += postfixStack.pop()
                postfixStack.append(x)
            else:
                postfixStack.append(x)
    while len(postfixStack) > 0:
        postfix += postfixStack.pop()

    numStack = []
    for x in postfix:
        if x.isdigit():
            numStack.append(x)
        else:
            if x == '+':
                ans = int(numStack.pop()) + int(numStack.pop())
            else:
                ans = int(numStack.pop()) * int(numStack.pop())
            numStack.append(ans)
    output = numStack.pop()
    print(f'#{tc} {output}')

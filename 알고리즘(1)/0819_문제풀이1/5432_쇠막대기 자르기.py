import sys
sys.stdin = open('5432.txt')
'''
() : 레이저
(((...))) : 쇠파이프 위에 짧은 쇠파이프를 올린 것.

'('가 나오면?
1. 레이저이거나
    -> 레이저면? 기존의 파이프 수 += len(stack)
2. 그냥 쇠파이프임
    -> stack에 +1, 파이프 수 +1

')'가 나오면?
stack에서 하나 pop
'''
T = int(input())
for tc in range(1, T+1):
    pipes = list(input())
    pipesStack = []

    i = 0
    cntPipe = 0
    while i < len(pipes):
        if pipes[i] == '(':
            if pipes[i+1] == ')':
                cntPipe += len(pipesStack)
                i += 2
            else:
                pipesStack.append(True)
                cntPipe += 1
                i += 1
        else:
            pipesStack.pop()
            i += 1
    print(f'#{tc} {cntPipe}')
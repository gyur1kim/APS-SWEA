import sys
sys.stdin = open('2635.txt')

N = int(input())
stack = [N]
maxStackLen = 0
maxStack = []
for i in range(int(N/2), N+1):
    stack.append(i)
    while True:
        newV = stack[-2] - stack[-1]
        if newV < 0:
            if maxStackLen < len(stack):
                maxStackLen = len(stack)
                maxStack = stack
            stack = [N]
            break
        else:
            stack.append(newV)

print(f'{maxStackLen}\n', *maxStack)
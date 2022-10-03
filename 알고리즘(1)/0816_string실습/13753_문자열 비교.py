import sys

sys.stdin = open('13753.txt')

T = int(input())
for t in range(1, T + 1):
    pattern = input()
    compareStr = input()

    print(f'pattern:{pattern}, compareStr:{compareStr}')

    lenP = len(pattern)
    patternDict = {}
    for i, v in enumerate(pattern):
        patternDict[v] = lenP - 1 - i
    print(patternDict)
    
import sys
sys.stdin = open('13753.txt')

T = int(input())
for t in range(1, T+1):
    pattern = input()
    compareStr = input()

    patterDict = {}
    for p in pattern:
        patterDict.update({p: 0})

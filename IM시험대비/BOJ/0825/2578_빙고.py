import sys
sys.stdin = open('2578.txt')

bingo = [list(map(int, input().split())) for _ in range(5)]
print(bingo)
called = [list(map(int, input().split())) for _ in range(5)]
print(called)
# rowDict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
# colDict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
# dig = {1:[]}
cnt = 0

i = j = 0
while True:
    nowNum = called[i][j]


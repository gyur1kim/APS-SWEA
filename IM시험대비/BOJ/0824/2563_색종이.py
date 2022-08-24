import sys
sys.stdin = open('2563.txt')

papers = int(input())
whitePaper = [[0] * 100 for _ in range(100)]

for _ in range(papers):
    X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    for i in range(Y, Y+10):
        for j in range(X, X+10):
            whitePaper[i][j] = 1

area = 0
for i in range(100):
    area += sum(whitePaper[i])
print(area)
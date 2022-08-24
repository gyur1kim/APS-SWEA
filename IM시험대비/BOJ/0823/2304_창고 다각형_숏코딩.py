import sys
sys.stdin = open('2304.txt')

n = int(input())
arr = [[*map(int, input().split())] for _ in range(n)]
info = [0]*(max(arr, key=lambda x: x[0])[0]+1)

for i, l in arr:
    info[i] = l
h = max(arr, key=lambda x: x[1])[0]
a = 0
m = 0
for i in range(0,h+1):
    m = max(m, info[i])
    a += m
b = 0
m = 0
for i in range(len(info)-1,h,-1):
    m = max(m, info[i])
    b += m
print(a+b)
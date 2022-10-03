import sys
sys.stdin = open('input.txt')

case = map(int, input())
lst = list(map(int, input().split()))

res = 0
for i in range(len(lst)):
    if lst[i] == 0:
        continue
    count = 0
    for j in range(i+1, len(lst)):
        if lst[i] > lst[j]:
            count += 1
    res = max(res, count)

print(res)
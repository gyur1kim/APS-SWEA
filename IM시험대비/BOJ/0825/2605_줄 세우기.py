import sys
sys.stdin = open('2605.txt')


studentsN = int(input())
numbers = list(map(int, input().split()))
line = []
for i, num in enumerate(numbers, 1):
    line[num:num] = [i]
print(*reversed(line))
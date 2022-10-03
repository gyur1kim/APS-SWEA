import sys
sys.stdin = open('13623.txt')

T = int(input())
for t in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))
    maxN = minN = nums[0]

    for i in range(1, n):
        if nums[i] > maxN:
            maxN = nums[i]
        if nums[i] < minN:
            minN = nums[i]

    print(f'#{t} {maxN-minN}')
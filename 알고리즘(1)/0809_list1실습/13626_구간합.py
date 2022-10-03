import sys
sys.stdin = open('13626.txt')

T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    addNums = []

    for i in range(0, n-m+1):
        addNums.append(sum(nums[i: i+m]))

    print(f'#{t} {max(addNums) - min(addNums)}')
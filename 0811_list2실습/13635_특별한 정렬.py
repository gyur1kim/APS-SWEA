import sys
sys.stdin = open('13635.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    for i in range(10):
        if i % 2:     #작은걸 찾아서 앞에거랑 자리바꾸기
            minIdx = i
            for j in range(i+1, N):
                if nums[j] < nums[minIdx]:
                    minIdx = j
            nums[minIdx], nums[i] = nums[i], nums[minIdx]
        else:       #큰걸 찾아서 앞에거랑 자리바꾸기
            maxIdx = i
            for j in range(i + 1, N):
                if nums[j] > nums[maxIdx]:
                    maxIdx = j
            nums[maxIdx], nums[i] = nums[i], nums[maxIdx]
    print(f'#{t} {" ".join(map(str, nums[:10]))}')
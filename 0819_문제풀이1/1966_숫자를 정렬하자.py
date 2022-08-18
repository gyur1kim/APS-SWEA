import sys
sys.stdin = open('1966.txt')

# 있어보이고 싶어서 나댔습니다...ㅈㅅ
# 나도 속도 빠르고싶단말야...
def mergeSort(lst):
    if len(lst) == 1:
        return lst
    mid = len(lst)//2
    left = lst[0:mid]
    right = lst[mid:]
    return merge(mergeSort(left), mergeSort(right))

def merge(left, right):
    ans = []
    while len(left) and len(right):
        if left[0] >= right[0]:
            ans.append(right.pop(0))
        else:
            ans.append(left.pop(0))
    return ans + right + left

T = int(input())
for tc in range(1, T+1):
    numLen = int(input())
    nums = list(map(int, input().split()))
    res = mergeSort(nums)
    print(f'#{tc}', *res)
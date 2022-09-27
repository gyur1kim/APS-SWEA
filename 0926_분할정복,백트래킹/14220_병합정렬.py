import sys
sys.stdin = open('14220.txt')


def mergeSort(lst):
    if len(lst) == 1:
        return lst

    mid = len(lst)//2
    left = lst[:mid]
    right = lst[mid:]
    return merge(mergeSort(left), mergeSort(right))


def merge(left, right):
    global cnt
    if left[-1] > right[-1]:
        cnt += 1
    res = []
    left = left[::-1]
    right = right[::-1]
    while left and right:
        res.append(right.pop()) if left[-1] > right[-1] else res.append(left.pop())
    return res + left[::-1] + right[::-1]


for tc in range(1, int(input())+1):
    l = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    mergeRes = mergeSort(arr)
    print(f'#{tc} {mergeRes[l//2]} {cnt}')
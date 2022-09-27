import sys
sys.stdin = open('14222.txt')


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())  # A에 속한 정수의 개수, B에 속한 정수의 개수
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    if tc != 4:
        continue
    cnt = 0

    for v in B:
        start = 0
        end = N - 1

        searchLeft = True
        searchRight = True

        while start <= end:
            mid = (start + end) // 2
            print(A[mid])
            if A[mid] == v:
                cnt += 1
                break
            elif A[mid] < v:      # 오른쪽을 뒤져보자
                if (searchLeft and not searchRight) or (searchLeft and searchRight):
                    searchLeft = False
                    searchRight = True
                elif not searchLeft and searchRight:
                    break
                start = mid + 1
            elif A[mid] > v:      # 왼쪽을 뒤져보자
                if (not searchLeft and searchRight) or (searchLeft and searchRight):
                    searchLeft = True
                    searchRight = False
                elif searchLeft and not searchRight:
                    break
                end = mid - 1

    print(f'#{tc} {cnt}')




# def binarysearch(n, key):
#     low = 0
#     high = n - 1
#     seq_lst = [0]
#     idx = 0
#     while low <= high:
#         mid = (low + high)//2
#         idx += 1
#         if lstA[mid] == key:
#             return 1
#         elif lstA[mid] > key:
#             high = mid - 1
#             seq_lst.append('L')
#         elif lstA[mid] < key:
#             low = mid + 1
#             seq_lst.append('R')
#
#         if seq_lst[idx - 1] == seq_lst[idx]:
#             return 0
#
#
# T = int(input())
# for t in range(1, T+1):
#     N, M = map(int, input().split())
#     lstA = list(map(int, input().split()))       # 길이 : N
#     lstB = list(map(int, input().split()))       # 길이 : M
#
#     cnt = 0
#     for key in lstB:
#         if key in lstA:
#             cnt += binarysearch(N, key)
#     print(f'#{t} {cnt}')
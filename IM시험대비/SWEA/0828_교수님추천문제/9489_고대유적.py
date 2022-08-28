import sys
sys.stdin = open('9489.txt')


# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [[0]*(M+2)]
#     arr.extend([[0] + list(map(int, input().split())) + [0] for _ in range(N)])
#     arr += [[0]*(M+2)]
#
#     longest = 0
#     for i in range(N+2):
#         cnt = 0
#         cntCol = 0
#         for j in range(M+2):
#             if arr[i][j]:
#                 cnt += 1
#             else:
#                 longest = cnt if cnt > longest else longest
#                 cnt = 0
#             if arr[j][i]:
#                 cntCol += 1
#             else:
#                 longest = cntCol if cntCol > longest else longest
#                 cntCol = 0
#     print(f'#{tc} {longest}')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*(M+2)]
    arr.extend([[0] + list(map(int, input().split())) + [0] for _ in range(N)])
    arr += [[0]*(M+2)]

    longest = 0
    for i in range(N+2):
        cnt = 0
        for j in range(M+2):
            if arr[i][j]:
                cnt += 1
            else:
                longest = cnt if cnt > longest else longest
                cnt = 0

    for i in range(M + 2):
        cnt = 0
        for j in range(N + 2):
            if arr[j][i]:
                cnt += 1
            else:
                longest = cnt if cnt > longest else longest
                cnt = 0
    print(f'#{tc} {longest}')
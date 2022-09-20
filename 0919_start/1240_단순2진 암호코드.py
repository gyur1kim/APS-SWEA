import sys
sys.stdin = open('1240.txt')


# def findCode(lst):
#     idx = 0
#     while True:
#         if row[idx:idx + 7] in codeDict:
#             codeSum = 0
#             validSum = 0
#             for j in range(0, 8):
#                 num = codeDict.get(row[idx + 7 * j: idx + 7 * (j + 1)], None)
#                 if num is None:
#                     idx += 1
#                     break
#                 codeSum += num
#                 validSum += num if j % 2 else num * 3
#             else:
#                 return print(f'#{tc} {codeSum if validSum % 10 == 0 else 0}')
#         else:
#             idx += 1


codeDict = {'0001101': 0,
            '0011001': 1,
            '0010011': 2,
            '0111101': 3,
            '0100011': 4,
            '0110001': 5,
            '0101111': 6,
            '0111011': 7,
            '0110111': 8,
            '0001011': 9}


# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())    # N은 세로, M은 가로
#     codeArr = [input() for _ in range(N)]
#
#     for row in codeArr:
#         if '1' in row:
#             findCode(row)
#             break




'''
코드의 규칙?을 보면 결국 마지막 자리수는 1이다.
따라서 그냥 rstrip을 하면 된다. 그러면 코드의 끝은 남아있게 된다!
이걸 이용해서 7개씩 자르면 된다. 너무 간단하잖아!
'''
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N은 세로, M은 가로
    code = ''
    for _ in range(N):
        codeLst = input().rstrip('0')
        if codeLst:
            code = codeLst[-56:]

    codeSum = 0
    validSum = 0
    for j in range(8):
        num = codeDict[code[7 * j: 7 * (j + 1)]]
        codeSum += num
        validSum += num if j % 2 else num*3
    print(f'#{tc} {codeSum if validSum % 10 == 0 else 0}')
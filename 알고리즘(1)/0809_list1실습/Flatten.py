import sys

sys.stdin = open('Flatten.txt')

# for n in range(1, 11):
#     cnt = int(input())
#     boxes = list(map(int, input().split()))
#     orderedBoxes = sorted(boxes)
#     minIdx = 0
#     maxIdx = 99
#     while orderedBoxes[minIdx] == orderedBoxes[minIdx+1]:
#         minIdx += 1
#     while orderedBoxes[maxIdx] == orderedBoxes[maxIdx - 1]:
#         maxIdx -= 1
#
#     while cnt > 0:
#         if minIdx == maxIdx:
#             break
#
#         orderedBoxes[minIdx] += 1
#         orderedBoxes[maxIdx] -= 1
#         minIdx -= 1
#         maxIdx += 1
#         if minIdx < 0:
#             minIdx = 0
#             while orderedBoxes[minIdx] == orderedBoxes[minIdx + 1]:
#                 minIdx += 1
#         if maxIdx > 99:
#             maxIdx = 99
#             while orderedBoxes[maxIdx] == orderedBoxes[maxIdx - 1]:
#                 maxIdx -= 1
#
#
#         cnt -= 1
#     print(f'#{n} {orderedBoxes[maxIdx] - orderedBoxes[minIdx]}');

# 인덱스를 왔다갔다
# for n in range(1, 11):
#     cnt = int(input())
#     boxes = list(map(int, input().split()))
#     orderedBoxes = sorted(boxes)
#     minIdx = 0
#     maxIdx = 99
#
#     while cnt > 0:
#         if minIdx == maxIdx:
#             break
#         orderedBoxes[minIdx] += 1
#         orderedBoxes[maxIdx] -= 1
#         if orderedBoxes[minIdx] <= orderedBoxes[minIdx+1]:
#             minIdx = 0
#         else:
#             minIdx += 1
#         if orderedBoxes[maxIdx] >= orderedBoxes[maxIdx-1]:
#             maxIdx = 99
#         else:
#             maxIdx -= 1
#         cnt -= 1
#     print(f'#{n} {orderedBoxes[maxIdx] - orderedBoxes[minIdx]}')

# 그냥 한 번 할때마다 정렬해버리면?
for n in range(1, 11):
    cnt = int(input())
    boxes = list(map(int, input().split()))
    boxes.sort()

    while cnt > 0:
        if boxes[0] == boxes[99]:
            break
        boxes[0] += 1
        boxes[99] -= 1
        boxes.sort()
        cnt -= 1
    print(f'#{n} {boxes[99] - boxes[0]}')
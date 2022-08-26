import sys
sys.stdin = open('13300.txt')


'''
같은 성별 같은 학생들끼리 배정할 것!
여학생 : 0
남학생 : 1
'''

studentsN, maxK = map(int, input().split())
mList = [[0] for _ in range(7)]
wList = [[0] for _ in range(7)]
# print(mList)
# print(wList)

for _ in range(studentsN):
    gender, year = map(int, input().split())
    if gender:    # 남학생이라면?
        mList[year][0] += 1
    else:         # 여학생이라면?
        wList[year][0] += 1

rooms = 0
for m in mList:
    room, rest = divmod(m[0], maxK)
    rooms += room if rest == 0 else (room+1)
for w in wList:
    room, rest = divmod(w[0], maxK)
    rooms += room if rest == 0 else (room+1)
print(rooms)
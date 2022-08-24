import sys
sys.stdin = open('2304.txt')

N = int(input())
pillars = [list(map(int, input().split())) for _ in range(N)]
pillars = sorted(pillars, key=lambda x: x[0])

# 젤 높은 기둥과 인덱스 찾기
highestPillar = 0
highestPillarIdx = 0
for i in range(N):
    if pillars[i][1] > highestPillar:
        highestPillar = pillars[i][1]
        highestPillarIdx = i

# 앞에서부터 보기
area = 0
nowHeight = pillars[0][1]
left = pillars[0][0]
i = 1
while i < highestPillarIdx:
    if pillars[i][1] > nowHeight:
        area += nowHeight * (pillars[i][0] - left)
        left = pillars[i][0]
        nowHeight = pillars[i][1]
    i += 1

area += (pillars[highestPillarIdx][0] - left) * nowHeight

# 뒤에서부터 보기
nowHeight = pillars[N - 1][1]
right = pillars[N-1][0] + 1
i = N-1-1
while i > highestPillarIdx:
    if pillars[i][1] > nowHeight:
        area += nowHeight * (right - (pillars[i][0]+1))
        right = pillars[i][0] + 1
        nowHeight = pillars[i][1]
    i -= 1
area += (right - (pillars[highestPillarIdx][0]+1)) * nowHeight

area += highestPillar
print(area)
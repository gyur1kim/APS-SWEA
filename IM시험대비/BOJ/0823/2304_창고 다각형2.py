import sys
sys.stdin = open('2304.txt')

N = int(input())
pillars = [list(map(int, input().split())) for _ in range(N)]
# 기둥 높이로 정렬하기
pillars.sort(key=lambda x: x[1], reverse=True)
pillarsDict = {}
# 기둥 높이로 딕셔너리 만들기, key는 기둥의 높이, value는 기둥의 위치?
for i in range(N):
    d = pillarsDict.get(pillars[i][1], [])
    d.append(pillars[i][0])
    pillarsDict[pillars[i][1]] = d

# 최대 기둥 높이 찾기
highestPillar = max(pillarsDict)
# 면적 구하기
left = right = 0
area = 0
for height, x in pillarsDict.items():   # 딕셔너리 순회하기
    if height == highestPillar:         # 만약 지금 높이가 최대 기둥 높이면(처음만 시행할거임)
        left = min(x)                   # 최대 기둥의 left right를 구한다
        right = max(x)+1
        area += height * (right - left) # 높이를 구한다
    else:
        # 최고기둥 기준 왼쪽 계산
        leftStart = min(x)
        if leftStart < left:
            area += height * (left - leftStart)
            left = leftStart
        # 최고기둥 기준 오른쪽 계산
        rightEnd = max(x) + 1
        if rightEnd > right:
            area += height * (rightEnd - right)
            right = rightEnd

print(area)
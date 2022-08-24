import sys
sys.stdin = open('2491.txt')

N = int(input())
arr = list(map(int, input().split()))

# 커지는 경우
caseBig = 0
tmp = []
for n in arr:
    if len(tmp) == 0:
        tmp.append(n)
    else:
        if tmp[-1] > n:
            caseBig = max(caseBig, len(tmp))
            tmp = [n]
        else:
            tmp.append(n)
caseBig = max(caseBig, len(tmp))

# 작아지는 경우
caseSmall = 0
tmp = []
for n in arr:
    if len(tmp) == 0:
        tmp.append(n)
    else:
        if tmp[-1] < n:
            caseSmall = max(caseSmall, len(tmp))
            tmp = [n]
        else:
            tmp.append(n)
    # print(tmp)
caseSmall = max(caseSmall, len(tmp))

print(max(caseBig, caseSmall))
import sys
input = sys.stdin.readline
sys.stdin = open('2559.txt')


day, k = map(int, input().split())  # 전체 날짜랑, 측정해야 하는 연속적인 날 k
temperatures = list(map(int, input().split()))
postTemp = maxTemp = sum(temperatures[:k])
for i in range(day - k):
    tmpTemp = postTemp - temperatures[i] + temperatures[i+k]
    postTemp = tmpTemp
    maxTemp = max(maxTemp, tmpTemp)
print(maxTemp)

import sys
sys.stdin = open('1959.txt')


T = int(input())
for T in range(1, T+1):
    lenN, lenM = map(int, input().split())
    arrN = list(map(int, input().split()))
    arrM = list(map(int, input().split()))

    if lenN > lenM:
        for i in range(lenN-lenM+1):
            lst = zip(arrN[i:i+lenM], arrM)
            ans = 0

    else:
        pass
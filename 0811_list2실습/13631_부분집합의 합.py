import sys
sys.stdin = open('13631.txt')

T = int(input())
setA = [i for i in range(1, 13)]
for t in range(1, T+1):
    size, sumSet = list(map(int, input().split()))

    res = 0
    for i in range(1 << 12):
        i2bin = format(i, 'b')
        binSumOne = sum(map(int, str(i2bin)))   # 이 숫자의 2진수에서 1이 n개면 원소가 n개인 부분집합이 만들어짐.
        if binSumOne == size:
            tmpSet = []
            for j in range(12):
                if i & (1 << j):
                    tmpSet.append(setA[j])
            if sum(tmpSet) == sumSet:
                res += 1
    print(f'#{t} {res}')
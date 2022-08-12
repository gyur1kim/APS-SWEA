import sys

sys.stdin = open('1221.txt')

numsDict = {'ZRO': 0, 'ONE': 1, 'TWO': 2,
            'THR': 3, 'FOR': 4, 'FIV': 5,
            'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
T = int(input())
for _ in range(T):
    t, nums = input().split()
    numsArr = input().split()
    numsCntArr = [0]*10
    for n in numsArr:
        numsCntArr[numsDict[n]] += 1

    print(t)
    for k, v in numsDict.items():
        print((k+' ') * numsCntArr[v], end='')
    print()
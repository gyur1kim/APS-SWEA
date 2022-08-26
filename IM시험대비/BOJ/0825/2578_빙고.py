import sys
sys.stdin = open('2578.txt')

'''
시현오빠 아이디어
1. 빙고가 완성되는 배열 만들기(가로 5개, 세로 5개, 대각선 2개)
2. 사회자가 부르는 값들을 집합에 넣기
3. 위에서 만든 배열이 사회자가 부른 값의 부분집합이 되면 모든 숫자가 불린 것이므로,
    cnt++를 한다.
4. cnt==3이 되면 멈추고, 그 때까지 사회자가 부른 숫자의 길이를 출력한다.
'''


def checkAns(ansSet):
    for i in range(11, 25):
        ansSet.add(answerNums[i])
        cnt = 0
        for l in answerList:
            if ansSet.issuperset(set(l)):
                cnt += 1
                if cnt == 3:
                    return len(ansSet)

# 빙고 자료 정리하기
bingo = [list(map(int, input().split())) for _ in range(5)]

answerList = []                 # 빙고가 되는 값들을 넣자
answerList.extend(bingo)        # extend를 이용하면 한번에 넣을 수 있음
bingoRev = list(zip(*bingo))    # 열을 넣기 위해 뒤집어주기
answerList.extend(bingoRev)     # 똑같이 넣자
d1 = []                         # 대각선 값을 넣을 배열 1
d2 = []                         # 대각선 값을 넣을 배열 2
for i in range(5):
    d1.append(bingo[i][i])
    d2.append(bingo[i][4-i])
answerList.append(d1)
answerList.append(d2)

# 이제 사회자가 부르는 값을 이용하자!
answerNums = []
for _ in range(5):
    answerNums.extend(list(map(int, input().split())))
answerSet = set(answerNums[:11])
print(checkAns(answerSet))


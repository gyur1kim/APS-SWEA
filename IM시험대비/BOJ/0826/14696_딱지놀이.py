import sys
sys.stdin = open('14696.txt')

'''
딱지놀이의 규칙
딱지 중 어느 것이 더 강력할까??
1. 별의 개수가 많은 쪽  (4)
2. 동그라미가 많은 쪽   (3)
3. 네모가 많은 쪽       (2)
4. 세모가 많은 쪽       (1)
5. 무승부               D 출력
'''


def checkWinner(tA, tB):
    global res
    while tA and tB:
        a = tA.pop()
        b = tB.pop()
        if a == b:
            continue
        elif a > b:
            res += 'A\n'
            return
        else:
            res += 'B\n'
            return
    if not tA or not tB:
        if len(tA) == len(tB) == 0:
            res += 'D\n'
        else:
            res += 'A\n' if len(tA) != 0 else 'B\n'


gameRound = int(input())
res = ''
for r in range(gameRound):
    aNum, *ttakjiA = list(map(int, input().split()))
    bNum, *ttakjiB = list(map(int, input().split()))
    ttakjiA.sort()
    ttakjiB.sort()
    checkWinner(ttakjiA, ttakjiB)
print(res)
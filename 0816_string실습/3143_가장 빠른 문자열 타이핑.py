import sys
sys.stdin = open('3143.txt')

T = int(input())
for t in range(1, T+1):
    strA, word = input().split()
    cnt = 0    # 타이핑의 횟수
    i = 0      # 패턴의 idx

    # 그냥 슬라이싱 쓸래...난 틀렸어
    
    print(f'strA:{strA}, word:{word}')
    print(f'#{t} {cnt}')
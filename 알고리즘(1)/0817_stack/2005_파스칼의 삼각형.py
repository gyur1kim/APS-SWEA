import sys
sys.stdin = open('2005.txt')

triangle = [[1], [1, 1]]
print(triangle)

def pascal(n):  # 여기서 들어오는 n은 인덱스로 보면 됨...
    global triangle
    if n < 3:
        return
    else:
        for i in range(2, n):    # 행
            if i >= len(triangle):   # 내가 보는 행이 triangle에 없으면 append할거임
                row = []
                for j in range(i-1):   # 열
                    row += [triangle[i - 1][j] + triangle[i - 1][j + 1]]
                triangle += [[1] + row + [1]]


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    pascal(n)

    print(f'#{tc}')
    for m in range(n):
        print(*triangle[m])

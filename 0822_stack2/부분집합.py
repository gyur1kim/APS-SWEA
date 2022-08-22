# 그냥 부분집합만 만들 뿐, 가지치기는 불가능하다
# def f(i, N):
#     if i == N:
#         for i in range(N):
#             if bit[i]:
#                 print(A[i], end = ' ')
#             print()
#         print(bit)
#     else:
#         bit[i] = 1
#         f(i+1, N)
#         bit[i] = 0
#         f(i+1, N)

# 가지치기 하는 함수 -> 실행횟수를 줄일 수 있음
def f2(i, N, s, t):
    global answer
    if i == N:
        if s == t:
            answer += 1
        return
    elif s > t:
        return
    else:
        f2(i+1, N, s+A[i], t)   # 부분집합 포함 경우
        f2(i+1, N, s, t)        # 부분집합 포함X 경우


A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * len(A)
# f(0, 3)
answer = 0
f2(0, len(A), 0, 10)
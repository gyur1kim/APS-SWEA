import sys
sys.stdin = open('1244.txt')


'''
남학생(1) : 자신이 받은 번호의 배수를 바꿈
여학생(2) : 자기가 받은 숫자 중심으로, 좌우가 대칭이면서 많은 스위치를 포함하는 구간을 찾음.
            구간에 속한 스위치 개수는 항상 홀수
'''

N = int(input())  # 스위치 개수
switches = list(map(int, input().split()))   # 스위치 받기

studentsN = int(input())                 # 학생 수
for _ in range(studentsN):               # 학생 수만큼 돌아봅시다
    s, num = map(int, input().split())   # 학생의 성별과, 학생이 받은 숫자 받기
    if s == 1:   # 남학생이면?
        for i in range(num-1, N, num):   # range의 step을 이용, num만큼 뛸거임, num-1인 이유는 숫자는 1부터 시작하니깐
            # switches[i] = abs(switches[i]-1)
            switches[i] = 0 if switches[i] else 1   # 값을 바꾸는 방법은 두 가지 존재함 ㅎㅎ 잘 생각해봐용
    elif s == 2:    # 여학생이면
        num -= 1    # 인덱스는 0부터 시작인데 스위치는 1부터 시작하잖아,,, 1 뺴자?
        switches[num] = abs(switches[num]-1)
        start = num - 1
        end = num + 1
        while start > -1 and end < N:              # 시작점이 0이상, 끝 점이 스위치길이보다 작을 때만 돌거임
            if switches[start] == switches[end]:   # 앞뒤로 같으면 바꾸기
                switches[start] = abs(switches[start] - 1)
                switches[end] = abs(switches[end] - 1)
                start -= 1
                end += 1
            else:                                   # 앞뒤로 달라지면 끝내기
                break

for i in range(0, N, 20):        # 20줄씩 출력하기
    print(*switches[i:i+20])
import time


def fibo(n):
    f = [0, 1]
    for i in range(2, n+1):
        f.append(f[i-2] + f[i-1])
    return f[n]


# 0.0초 걸림 빠르네...
start = time.time()
print(fibo(40))
print(time.time() - start)
import time

def fibo(n):
    # global memo
    if n >= 2 and len(memo) <= n:
        memo.append(fibo(n - 1) + fibo(n - 2))
    return memo[n]


def fibo2(n):
    if n < 2:
        return n
    else:
        return fibo2(n - 1) + fibo2(n - 2)

# 0.0초 걸림
start = time.time()
memo = [0, 1]
print(fibo(40))
print(time.time() - start)

# 17.47초 걸림
start = time.time()
print(fibo2(40))
print(time.time() - start)
def f(i, k):
    if i == k:
        for b in range(n):
            if bit[b]:
                print(arr[b], end=" ")
        print()
    else:
        bit[i] = 0
        f(i+1, k)
        bit[i] = 1
        f(i+1, k)


arr = [3, 6, 7, 1, 5, 4]
n = len(arr)
bit = [0] * n
f(0, n)
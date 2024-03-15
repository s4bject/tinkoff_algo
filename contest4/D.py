def k_number(n, k):
    l, r = 1, n * n
    while l < r:
        mid = (l + r) // 2
        count = 0
        for i in range(1, n + 1):
            count += min(mid // i, n)
        if count < k:
            l = mid + 1
        else:
            r = mid
    return l

n, k = map(int, input().split())
print(k_number(n, k))
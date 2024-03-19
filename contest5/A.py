def z_function(s, a, b):
    n = b - a
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[a + z[i]] == s[a + i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z


def substrings(s, a, b, c, d):
    z1 = z_function(s, a - 1, b)
    z2 = z_function(s, c - 1, d)
    return z1 == z2 and s[a - 1:b] == s[c - 1:d]

s = input().strip()
m = int(input().strip())
for _ in range(m):
    a, b, c, d = map(int, input().split())
    if substrings(s, a, b, c, d):
        print("Yes")
    else:
        print("No")

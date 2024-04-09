def update(i, j):
    dp[i][j] += dp[i - 2][j - 1] + dp[i - 2][j + 1] + dp[i - 1][j - 2] + dp[i + 1][j - 2]

n, m = map(int, input().split())
n += 2
m += 2
dp = [[0] * (m + 1) for _ in range(n + 1)]
dp[2][2] = 1
i, j = 2, 2
while i != n - 1 or j != m - 1:
    x, y = i, j
    while x >= 2 and y < m:
        update(x, y)
        x -= 1
        y += 1
    if i == n - 1:
        j += 1
    else:
        i += 1
update(n - 1, m - 1)
print(dp[n - 1][m - 1])

def boom(n):
    dp = [[[0 for _ in range(2)] for _ in range(3)] for _ in range(n + 1)] # стопки\последний контейнер\сколько А
    for prev_type in range(3):
        dp[1][prev_type][0] = 1
    for stack_size in range(2, n + 1):
        for prev_type in range(3):
            for curr_type in range(3):
                for consecutive_A in range(2):
                    if curr_type == 0:
                        if prev_type == 0:
                            continue
                        new_consecutive_A = consecutive_A + 1
                    else:
                        new_consecutive_A = 0
                    if new_consecutive_A <= 1:
                        dp[stack_size][curr_type][consecutive_A] += dp[stack_size - 1][prev_type][consecutive_A]

    count = sum(sum(dp[n][j]) for j in range(3))
    return count

n = int(input())
print(boom(n))

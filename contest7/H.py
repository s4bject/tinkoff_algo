def task_h(n, sequence):
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if sequence[i] > sequence[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    max_length = max(dp)
    max_index = dp.index(max_length)
    lis = []
    lis.append(sequence[max_index])
    current_length = max_length - 1
    current_index = max_index - 1
    while current_length > 0 and current_index >= 0:
        if dp[current_index] == current_length and sequence[current_index] < lis[-1]:
            lis.append(sequence[current_index])
            current_length -= 1
        current_index -= 1

    return max_length, lis[::-1]

n = int(input())
sequence = list(map(int, input().split()))
length, lis = task_h(n, sequence)
print(length)
print(*lis)

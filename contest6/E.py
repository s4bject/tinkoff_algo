from collections import deque


def find_min_sum(K):
    visited = [False] * K
    prev_remainder = [-1] * K
    digit_to_add = [-1] * K
    queue = deque([0])

    while queue:
        remainder = queue.popleft()
        if remainder == 0:
            break
        for digit in range(10):
            next_remainder = (remainder * 10 + digit) % K
            if not visited[next_remainder]:
                visited[next_remainder] = True
                prev_remainder[next_remainder] = remainder
                digit_to_add[next_remainder] = digit
                queue.append(next_remainder)

    if remainder != 0:
        return 0

    min_sum = 0
    while remainder != -1:
        min_sum += digit_to_add[remainder]
        remainder = prev_remainder[remainder]

    return min_sum


# Чтение входных данных
K = int(input())

# Вычисление и вывод результата
result = find_min_sum(K)
print(result)

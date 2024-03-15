def bubble_count(n, positions):
    count_last = n
    count_1 = 0
    mp = [0] * n
    iterations_count = [1]

    for pos in positions:
        if mp[pos - 1] == 0:
            mp[pos - 1] = 1
            count_1 += 1
            if count_last != count_1:
                while count_last > 0 and mp[count_last - 1] == 1:
                    count_last -= 1

        iterations = count_1 - (n - count_last) + 1
        iterations_count.append(iterations)

    return iterations_count

n = int(input())
positions = list(map(int, input().split()))

print(*bubble_count(n, positions)[:-1], 1)
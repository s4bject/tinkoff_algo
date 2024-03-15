def table_cut(n, m, goriz, vert):
    min_diff = float('inf')
    cut_position = 0

    goriz_prefix_sum = [0]
    for i in range(n):
        goriz_prefix_sum.append(goriz_prefix_sum[-1] + goriz[i])

    vert_prefix_sum = [0]
    for j in range(m):
        vert_prefix_sum.append(vert_prefix_sum[-1] + vert[j])

    for i in range(1, n + 1):
        diff = abs(goriz_prefix_sum[i] - goriz_prefix_sum[n] + goriz_prefix_sum[i])
        if diff < min_diff:
            min_diff = diff
            cut_position = i + 1

    for j in range(1, m + 1):
        diff = abs(vert_prefix_sum[j] - vert_prefix_sum[m] + vert_prefix_sum[j])
        if diff < min_diff:
            min_diff = diff
            cut_position = -(j + 1)

    return f"{'H' if cut_position > 0 else 'V'} {abs(cut_position)}"

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    goriz = [sum(range((i - 1) * m + 1, i * m + 1)) for i in range(1, n + 1)]
    vert = [sum(range(i, n * m + 1, m)) for i in range(1, m + 1)]
    print(table_cut(n, m, goriz, vert))
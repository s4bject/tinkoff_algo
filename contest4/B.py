def calculate_prefix_sums(matrix):
    prefix_sums = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]

    for i in range(1, len(matrix) + 1):
        for j in range(1, len(matrix[0]) + 1):
            prefix_sums[i][j] = prefix_sums[i-1][j] + prefix_sums[i][j-1] - prefix_sums[i-1][j-1] + matrix[i-1][j-1]

    return prefix_sums

def query_sum(prefix_sums, x1, y1, x2, y2):
    return prefix_sums[y2][x2] - prefix_sums[y1-1][x2] - prefix_sums[y2][x1-1] + prefix_sums[y1-1][x1-1]

N, M, K = map(int, input().split())

matrix = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)
prefix_sums = calculate_prefix_sums(matrix)

for _ in range(K):
    y1, x1, y2, x2 = map(int, input().split())
    print(query_sum(prefix_sums, x1, y1, x2, y2))
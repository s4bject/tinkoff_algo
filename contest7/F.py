def find_max_square(n, m, grid):
    right = [[0] * m for _ in range(n)]
    down = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                right[i][j] = right[i][j - 1] + 1 if j > 0 else 1
                down[i][j] = down[i - 1][j] + 1 if i > 0 else 1
    max_side_length = 0
    top_left_x = 0
    top_left_y = 0

    for i in range(n):
        for j in range(m):
            side_length = min(right[i][j], down[i][j])
            while side_length > max_side_length:
                if down[i][j - side_length + 1] >= side_length and right[i - side_length + 1][j] >= side_length:
                    max_side_length = side_length
                    top_left_x = i - side_length + 1
                    top_left_y = j - side_length + 1
                side_length -= 1

    return max_side_length, top_left_x, top_left_y

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
side_length, top_left_x, top_left_y = find_max_square(n, m, grid)
print(side_length, top_left_x, top_left_y)

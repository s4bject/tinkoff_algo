import queue

def hungry_horse(n,x1,x2,y1,y2):
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    steps = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
    q = queue.Queue()
    dist = [[-1] * n for i in range(n)]
    dist[x1][y1] = 0
    parent = [[None] * n for i in range(n)]
    q.put((x1, y1))

    while not q.empty():
        vx, vy = q.get()
        for dx, dy in steps:
            tx, ty = vx + dx, vy + dy
            if 0 <= tx < n and 0 <= ty < n and dist[tx][ty] == -1:
                q.put((tx, ty))
                dist[tx][ty] = dist[vx][vy] + 1
                parent[tx][ty] = (vx, vy)

    path = []
    current_x, current_y = x2, y2
    while (current_x, current_y) != (x1, y1):
        path.append((current_x + 1, current_y + 1))
        current_x, current_y = parent[current_x][current_y]
    path.append((x1 + 1, y1 + 1))
    path.reverse()
    return path


n = int(input())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
path = hungry_horse(n,x1,x2,y1,y2)
print(len(path) - 1)
for point in path:
    print(point[0], point[1])

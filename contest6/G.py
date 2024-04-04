INF = 10 ** 9

def floyd_warshall(graph, N):
    dist = [[INF] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                dist[i][j] = 0
            elif (i, j) in graph:
                dist[i][j] = graph[(i, j)]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist


def offline_sem(N, roads):
    graph = {}
    for u, v, w in roads:
        graph[(u - 1, v - 1)] = w
        graph[(v - 1, u - 1)] = w
    dist = floyd_warshall(graph, N)
    min_max_distance = INF
    city = -1
    for i in range(N):
        max_distance = max(dist[i])
        if max_distance < min_max_distance:
            min_max_distance = max_distance
            city = i + 1
    return city


N, M = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(M)]
print(offline_sem(N, roads))

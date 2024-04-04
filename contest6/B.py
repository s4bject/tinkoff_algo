def has_cycle(graph):
    visited = [False] * len(graph)
    stack = [False] * len(graph)

    def dfs(node):
        visited[node] = True
        stack[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
            elif stack[neighbor]:
                return True
        stack[node] = False
        return False

    for node in range(len(graph)):
        if not visited[node]:
            if dfs(node):
                return 1
    return 0

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)

print(has_cycle(graph))

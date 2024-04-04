
def dfs(start_node, graph, visited):
    stack = [start_node]
    component = []
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            component.append(node)
            stack.extend(neighbor for neighbor in graph[node] if not visited[neighbor])
    return component
def find_components(N, graph):
    visited = [False] * (N + 1)
    components = []
    for node in range(1, N + 1):
        if not visited[node]:
            component = dfs(node, graph, visited)
            components.append(component)
    return components

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

components = find_components(N, graph)
print(len(components))
for component in components:
    component.sort()
    print(len(component))
    print(*component)

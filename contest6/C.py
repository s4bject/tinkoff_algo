def is_topological(n,edges, shuffle):
    positions = {shuffle[i]: i for i in range(n)}
    for u, v in edges:
        if positions[u] > positions[v]:
            return "NO"
    return "YES"


n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
shuffle = list(map(int, input().split()))

result = is_topological(n, edges, shuffle)
print(result)

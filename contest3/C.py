from collections import defaultdict

def preprocess(n, tree):
    log_n = (n + 1).bit_length()
    parent = [[-1] * log_n for _ in range(n)]

    for v in range(n):
        for j in range(len(tree[v])):
            parent[tree[v][j]][0] = v

    for j in range(1, log_n):
        for i in range(n):
            if parent[i][j-1] != -1:
                parent[i][j] = parent[parent[i][j-1]][j-1]

    return parent, log_n

def lca(u, v, parent, log_n):
    if depth[u] < depth[v]:
        u, v = v, u

    for i in range(log_n - 1, -1, -1):
        if depth[u] - (1 << i) >= depth[v]:
            u = parent[u][i]

    if u == v:
        return u

    for i in range(log_n - 1, -1, -1):
        if parent[u][i] != parent[v][i]:
            u = parent[u][i]
            v = parent[v][i]

    return parent[u][0]

def dfs(node, depth, parent, tree):
    depth[node] = depth[parent] + 1
    for child in tree[node]:
        if child != parent:
            dfs(child, depth, node, tree)

n = int(input())
tree_input = list(map(int, input().split()))
m = int(input())

tree = defaultdict(list)
for i, parent in enumerate(tree_input):
    tree[parent].append(i + 1)

depth = [-1] * n
depth[0] = 0
dfs(0, depth, 0, tree)

parent, log_n = preprocess(n, tree)

for _ in range(m):
    u, v = map(int, input().split())
    print(lca(u, v, parent, log_n))

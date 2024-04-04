from collections import defaultdict, deque


def find_min_reactions(reactions, start, target):
    graph = defaultdict(list)
    for reaction in reactions:
        src, dest = reaction.split(" -> ")
        graph[src].append(dest)
    visited = set()
    queue = deque([(start, 0)])
    while queue:
        current, steps = queue.popleft()
        if current == target:
            return steps
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append((neighbor, steps + 1))
    return -1



m = int(input())
reactions = [input() for _ in range(m)]
start = input()
target = input()
print(find_min_reactions(reactions, start, target))

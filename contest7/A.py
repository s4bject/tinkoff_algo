def min_cost_steps(costs,n):
    min_cost = [0] * n
    min_cost[0] = costs[0]
    for i in range(1, n):
        min_cost[i] = min(min_cost[i - 1] + costs[i], min_cost[i - 2] + costs[i])
    return min_cost[n-1]

n = int(input())
costs = list(map(int, input().split()))
print(min_cost_steps(costs,n))
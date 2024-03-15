def sumxor(array, queries):
    n = len(array)
    cumulative_xor = [0] * (n + 1)
    prefix_sum = [0] * (n + 1)

    for i in range(n):
        cumulative_xor[i + 1] = cumulative_xor[i] ^ array[i]
        prefix_sum[i + 1] = prefix_sum[i] + array[i]

    result = []
    for query in queries:
        operation_type, l, r = query
        if operation_type == 1:
            result.append(prefix_sum[r] - prefix_sum[l - 1])
        elif operation_type == 2:
            result.append(cumulative_xor[r] ^ cumulative_xor[l - 1])

    return result

n = int(input())
array = list(map(int, input().split()))
m = int(input())

queries = []
for _ in range(m):
    query = list(map(int, input().split()))
    queries.append(query)

results = sumxor(array, queries)

for res in results:
    print(res)
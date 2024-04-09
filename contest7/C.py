def count_max_gold(n, k, ar):
    max_gold = 0
    max_gold_idx = 0
    path = []

    cur_gold = 0
    cur_path = []

    for i in range(n):
        cur_gold += ar[i]

        if len(cur_path) > 0 and i - cur_path[0] > k:
            cur_gold -= ar[cur_path.pop(0)]

        if cur_gold > max_gold:
            max_gold = cur_gold
            max_gold_idx = i

        cur_path.append(i)

    idx = max_gold_idx
    while idx >= 0:
        path.append(idx + 1)
        idx -= cur_path[idx]

    path.reverse()
    return max_gold, path


if __name__ == '__main__':
    n, k = map(int, input().split())
    ar = list(map(int, input().split()))

    max_gold, path = count_max_gold(n, k, ar)

    print(max_gold)
    print(len(path) - 1)
    print(" ".join(map(str, path)))

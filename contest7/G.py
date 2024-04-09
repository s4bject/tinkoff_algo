from collections import defaultdict

INF = 10**10


def get_optimal_splits(input_str):
    n = len(input_str)
    split_ind = defaultdict(lambda: -1)
    split_loss = defaultdict(lambda: INF)
    for i in range(n):
        split_ind[(i, i)] = i
        split_loss[(i, i)] = 1
        split_loss[(i, i - 1)] = 0
    for length in range(1, n):
        for i in range(n - length):
            j = i + length
            if ((input_str[i] == "[" and input_str[j] == "]") or
                    (input_str[i] == "(" and input_str[j] == ")") or
                    (input_str[i] == "{" and input_str[j] == "}")):
                split_loss[(i, j)] = split_loss[(i + 1, j - 1)]

            for k in range(i, j):
                current_loss = split_loss[(i, k)] + split_loss[(k + 1, j)]
                if current_loss < split_loss[(i, j)]:
                    split_loss[(i, j)] = current_loss
                    split_ind[(i, j)] = k

    return split_ind


def construct_balanced_string(input_str, split_ind, key):
    if key[1] - key[0] <= 0:
        return ""
    elif split_ind[key] == -1:
        return input_str[key[0]] + construct_balanced_string(input_str, split_ind, (key[0] + 1, key[1] - 1)) + input_str[key[1]]
    else:
        return (construct_balanced_string(input_str, split_ind, (key[0], split_ind[key])) +
                construct_balanced_string(input_str, split_ind, (split_ind[key] + 1, key[1])))


input_str = input()
split_ind = get_optimal_splits(input_str)
key = (0, len(input_str) - 1)
balanced_string = construct_balanced_string(input_str, split_ind, key)
print(balanced_string)

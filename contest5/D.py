def find_minimum(s):
    n = len(s)
    min_shift = s
    for i in range(1, n):
        current_shift = s[i:] + s[:i]
        if current_shift < min_shift:
            min_shift = current_shift
    return min_shift

s = input()
result = find_minimum(s)
print(result)

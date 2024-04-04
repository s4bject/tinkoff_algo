def find_approximate_matches(p, t):
    matches = []
    for i in range(len(t) - len(p) + 1):
        mismatch_count = 0
        for j in range(len(p)):
            if t[i + j] != p[j]:
                mismatch_count += 1
                if mismatch_count > 1:
                    break
        if mismatch_count <= 1:
            matches.append(i + 1)
    return matches

p = input().strip()
t = input().strip()
positions = find_approximate_matches(p, t)

print(len(positions))
print(*positions)


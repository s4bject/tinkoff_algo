def build_prefix(s):
    m = len(s)
    pi = [0] * m
    k = 0
    for q in range(1, m):
        while k > 0 and s[k] != s[q]:
            k = pi[k - 1]
        if s[k] == s[q]:
            k += 1
        pi[q] = k
    return pi

def redactor(s, sub_s):
    n = len(s)
    m = len(sub_s)
    pi = build_prefix(sub_s)
    q = 0
    index = []
    for i in range(n):
        while q > 0 and sub_s[q] != s[i]:
            q = pi[q - 1]
        if sub_s[q] == s[i]:
            q += 1
        if q == m:
            index.append(i - m + 1)
            q = pi[q - 1]
    return index

T = input().strip()
q = int(input().strip())
for _ in range(q):
    si = input().strip()
    index = redactor(T, si)
    print(len(index), *index)

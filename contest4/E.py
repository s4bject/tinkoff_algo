n = int(input())
l1,r1 = 10**9,-(10**9)
for _ in range(n):
    l,r = list(map(int, input().split()))
    if l < l1:
        l1 = l
    if r > r1:
        r1 = r
print(r1-l1)
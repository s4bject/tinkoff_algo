def f(x):
    return a * x**3 + b * x**2 + c * x + d

a, b, c, d = map(float, input().split())

r = 1
while f(r) * f(-r) >= 0:
    r *= 2

l = -r

while r - l > 1e-6:
    mid = (l + r) / 2
    if f(mid) * f(r) > 0:
        r = mid
    else:
        l = mid

print(l)
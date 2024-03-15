import math

def powsqrtpowpow(C):
    l, r = 0, C + 1

    while r - l > 1e-6:
        mid = (l + r) / 2
        f_mid = mid**2 + math.sqrt(mid + 1) - C

        if f_mid < 0:
            l = mid
        else:
            r = mid

    return round((l + r) / 2, 10)

C = float(input())
print(powsqrtpowpow(C))
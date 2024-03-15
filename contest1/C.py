from sys import stdout


def binary_search_quess(n_arr):
    l, r = 0, len(n_arr) - 1
    while l <= r:
        mid = (l + r) // 2
        print(mid)
        x = input()
        stdout.flush()
        if l == mid and x == ">=":
            return l;
        if r == mid and x == ">=":
            return r;
        if x == '<':
            r = mid
        else:
            l = mid
    return l

n= int(input())
n_arr = list(range(1,n + 3))
print("! " + str(binary_search_quess(n_arr)))

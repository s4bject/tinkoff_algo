def binary_search(arr, question):
    l, r = 0, len(arr) - 1

    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == question:
            return True
        elif arr[mid] < question:
            l = mid + 1
        else:
            r = mid - 1

    return False

n, k = map(int, input().split())
n_arr = list(map(int, input().split()))
q = list(map(int, input().split()))

for i in q:
    if binary_search(n_arr, i):
        print("YES")
    else:
        print("NO")
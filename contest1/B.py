def binary_search_near(arr, question):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == question:
            return arr[mid]
        elif arr[mid] < question:
            l = mid + 1
        else:
            r = mid - 1
    if r < 0:
        return arr[l]
    if l >= len(arr):
        return arr[r]
    if abs(arr[l] - question) >= abs(arr[r] - question):
        return arr[r]
    else:
        return arr[l]

n, k = map(int, input().split())
n_arr = list(map(int, input().split()))
q = list(map(int, input().split()))

for i in q:
    print(binary_search_near(n_arr, i))
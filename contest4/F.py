def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    l, inv_l = merge_sort(arr[:mid])
    r, inv_r = merge_sort(arr[mid:])
    merged, inv_merge = merge(l, r)

    return merged, inv_l + inv_r + inv_merge

def merge(l, r):
    result = []
    inv_count = 0
    i = j = 0

    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            inv_count += len(l) - i
            j += 1

    result.extend(l[i:])
    result.extend(r[j:])

    return result, inv_count

n = int(input())
arr = list(map(int, input().split()))

sorted_arr, inversions = merge_sort(arr)

print(inversions)
print(' '.join(map(str, sorted_arr)))
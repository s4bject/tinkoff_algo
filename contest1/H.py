def count_char(arr):
    nums = {}
    for i in arr:
        if i in nums:
            nums[i] += 1
        else:
            nums[i] = 1
    sorted_nums = dict(sorted(nums.items()))
    return sorted_nums
def palin(arr,n):
    res = [""] * n
    l = 0
    r = len(res) - 1
    mid = (l + r) // 2
    for i in arr:
        if arr[i] % 2 != 0:
            res[mid] = i
            arr[i] -= 1
            break
    for i in arr:
        if arr[i] >= 2:
            while arr[i] > 1:
                res[l] = i
                res[r] = i
                l += 1
                r -= 1
                arr[i] -= 2
        elif arr[i] == 1:
            continue

    return ''.join(res).strip()



n = int(input())
arr = input()
sorted_arr = count_char(arr)
print(palin(sorted_arr,n))
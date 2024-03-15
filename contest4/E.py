def count_segments(nums, max_sum):
    segments = 1
    current_sum = 0
    for num in nums:
        current_sum += num
        if current_sum > max_sum:
            segments += 1
            current_sum = num
    return segments

def min_max_segment_sum(nums, k):
    l = max(nums)
    r = sum(nums)
    while l < r:
        mid = (l + r) // 2
        segments = count_segments(nums, mid)

        if segments <= k:
            r = mid
        else:
            l = mid + 1
    return l

n, k = map(int, input().split())
nums = list(map(int, input().split()))
print(min_max_segment_sum(nums, k))
def gooddays(nums,n):
    min_prod = 0
    stack = []
    for i in range(n):
        i_sum = 0
        while stack and stack[-1][0] >= nums[i]:
            j, j_sum = stack.pop()
            min_prod = max(min_prod, j * (i_sum + j_sum))
            i_sum += j_sum
        stack.append([nums[i], i_sum + nums[i]])

    c_sum = 0
    while stack:
        j, j_sum = stack.pop()
        c_sum += j_sum
        min_prod = max(min_prod, j * c_sum)
    return min_prod


n = int(input())
nums = list(map(int,input().split()))
print(gooddays(nums,n))
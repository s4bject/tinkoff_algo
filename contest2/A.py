def stack(arr,a,stack_min):
    if a[0] == '1':
        arr.append(int(a[1]))
        if not stack_min or int(a[1]) <= stack_min[-1]:
            stack_min.append(int(a[1]))
    elif a[0] == '2':
        if arr[-1] == stack_min[-1]:
            stack_min.pop()
        arr.pop(-1)
    elif a[0] == '3':
        print(stack_min[-1])



n = int(input())
arr = []
stack_min = []
for _ in range(n):
    a = input().split()
    stack(arr,a,stack_min)
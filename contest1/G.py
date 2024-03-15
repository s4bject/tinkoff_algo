def anty_quick(arr,n):
    for i in range(2,n):
        arr[i],arr[i//2] = arr[i//2],arr[i]


n = int(input())
arr = list(range(1,n+1))
anty_quick(arr,n)
print(*arr)
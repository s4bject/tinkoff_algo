from collections import deque


def window(arr, k):
    mins = []
    deq = deque()
    for i in range(len(arr)):
        if (len(deq) > 0) and (deq[0] <= i - k):
            deq.popleft()
        while len(deq) > 0 and arr[deq[-1]] >= arr[i]:
            deq.pop()

        deq.append(i)

        if i >= k - 1:
            mins.append(arr[deq[0]])

    return mins

n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
print(*window(arr, k))
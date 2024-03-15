def can_place_cows(stalls, distance, cows):
    count_cows = 1
    last_position = stalls[0]
    for stall in stalls[1:]:
        if stall - last_position >= distance:
            count_cows += 1
            last_position = stall

            if count_cows == cows:
                return True

    return False

def largest_min_distance(stalls, cows):
    low, high = 1, stalls[-1] - stalls[0]

    while low <= high:
        mid = (low + high) // 2

        if can_place_cows(stalls, mid, cows):
            low = mid + 1
        else:
            high = mid - 1

    return high

N, K = map(int, input().split())
stalls = list(map(int, input().split()))

result = largest_min_distance(stalls, K)
print(result)
def seg(segments):
    balanced = 0
    s = 0
    result = 0
    for segment in segments:
        if balanced > 0:
            result += segment[0] - s
        balanced += segment[-1]
        s = segment[0]
    return result

n = int(input())
segments = []
for _ in range(n):
    l,r = map(int, input().split())
    segments.append([l,1])
    segments.append([r,-1])
segments.sort()
print(seg(segments))
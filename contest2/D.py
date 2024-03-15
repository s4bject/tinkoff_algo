def count_destroyed_balls(colors):
    stack = []
    destroyed = 0
    for color in colors:
        if stack and stack[-1][-1] == color:
            stack[-1].append(color)
        else:
            if stack and len(stack[-1]) >= 3:
                destroyed += len(stack[-1])
                stack.pop()
            if stack and stack[-1][-1] == color:
                stack[-1].append(color)
            else:
                stack.append([color])
    if stack and len(stack[-1]) >= 3:
        destroyed += len(stack[-1])
        stack.pop()


    return destroyed

n = int(input())
colors = list(map(int, input().split()))
print(count_destroyed_balls(colors))
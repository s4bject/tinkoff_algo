from collections import deque
import sys

def goblins(queries):
    queue1 = deque()
    queue2 = deque()
    k1 = 0
    k2 = 0

    for query in queries:
        if query[0] == '+':
            queue2.append(query[1])
            k2 += 1
        elif query[0] == '*':
            queue2.appendleft(query[1])
            k2 += 1
        elif query[0] == '-':
            sys.stdout.write(str(queue1.popleft()) + '\n')
            k1 -= 1
        if k1 < k2:
            queue1.append(queue2.popleft())
            k2 -= 1
            k1 += 1

n = int(input())
queries = [input().split() for _ in range(n)]
goblins(queries)
from collections import deque
def astrograd(events):
    queue = deque()
    idpositions = {}
    position = 0

    for event in events:
        event_type, *id = event
        if event_type == 1:
            queue.append(id[0])
            idpositions[id[0]] = position
            position += 1
        elif event_type == 2:
            removed_id = queue.popleft()
            del idpositions[removed_id]
            for person_id in queue:
                idpositions[person_id] -= 1
            position -= 1
        elif event_type == 3:
            removed_id = queue.pop()
            del idpositions[removed_id]
            position -= 1
        elif event_type == 4:
            print(idpositions[id[0]])
        elif event_type == 5:
            print(queue[0])


n = int(input())
events = []
for i in range(n):
    events.append(list(map(int,input().split())))

astrograd(events)
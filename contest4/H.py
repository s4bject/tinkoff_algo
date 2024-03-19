def maxtasks(c, tasks):
    sorted_tasks = sorted(enumerate(tasks, start=1), key=lambda x: x[1][0] + x[1][1])

    selected_tasks = []
    current_time = 0

    for task_number, task in sorted_tasks:
        if task[0] >= current_time:
            selected_tasks.append(task_number)
            current_time = task[0] + task[1]

    max_points = len(selected_tasks) * c

    return max_points, selected_tasks
n, c = map(int, input().split())
tasks = []
for _ in range(n):
    tasks.append(list(map(int, input().split())))
max_points, selected_tasks = maxtasks(c, tasks)
print(max_points)
print(len(selected_tasks))
print(*selected_tasks)

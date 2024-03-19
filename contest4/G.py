def total_working_time(N, schedules):
    time_sec = []
    for schedule in schedules:
        opening_hour, opening_minute, opening_second, closing_hour, closing_minute, closing_second = schedule
        opening_seconds = opening_hour * 3600 + opening_minute * 60 + opening_second
        closing_seconds = closing_hour * 3600 + closing_minute * 60 + closing_second
        if opening_seconds < closing_seconds:
            time_sec.append((opening_seconds, 1))
            time_sec.append((closing_seconds, -1))
        elif opening_seconds == closing_seconds:
            time_sec.append((0, 1))
            time_sec.append((24 * 3600, -1))
        else:
            time_sec.append((opening_seconds, 1))
            time_sec.append((24 * 3600, -1))
            time_sec.append((0, 1))
            time_sec.append((closing_seconds, -1))
    time_sec.sort()
    total_time = 0
    opened_count = 0
    prev_time = 0
    for time, change in time_sec:
        total_time += (time - prev_time) * (opened_count == N)
        opened_count += change
        prev_time = time

    return total_time


N = int(input())
schedules = []
for _ in range(N):
    schedule = list(map(int, input().split()))
    schedules.append(schedule)
total_time = total_working_time(N, schedules)
print(total_time)

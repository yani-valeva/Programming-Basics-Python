hours = int(input())
minutes = int(input())
time_after_15 = (hours * 60) + minutes + 15
total_hours = time_after_15 // 60
total_mins = time_after_15 % 60
if total_hours == 24:
    total_hours = 0
print('{0:}:{1:02d}' .format(total_hours, total_mins))
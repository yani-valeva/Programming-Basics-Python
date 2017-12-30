import math
days = int(input())
km = float(input())
total_km = km

for i in range(0, days):
    percent = int(input())
    km += km * (percent / 100)
    total_km += km

if total_km >= 1000:
    print('You\'ve done a great job running {0} more kilometers!'.format(math.ceil(total_km - 1000)))
else:
    print('Sorry Mrs. Ivanova, you need to run {0} more kilometers'.format(math.ceil(1000 - total_km)))
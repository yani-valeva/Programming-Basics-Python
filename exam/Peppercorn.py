import math
pepper_kg = float(input())
kg_per_hour = float(input())
petar_kg_per_hour = float(input())
ganio_kg_per_hour = float(input())
hours = float(input())

total = hours * kg_per_hour

if pepper_kg <= total:
    print('YES')
else:
    difference = pepper_kg - total
    time_for_kg = 1.0 / kg_per_hour
    needed_hours = difference * time_for_kg
    print('NO - {0}'.format(math.ceil(needed_hours)))
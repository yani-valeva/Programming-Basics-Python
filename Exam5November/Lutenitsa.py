import math
tomatoes_kg = float(input())
truck_boxes_count = int(input())
truck_jar_count = int(input())

total_kg_lutenitsa = tomatoes_kg / 5
jars = total_kg_lutenitsa / 0.535
boxes = jars / truck_jar_count

boxes_diff = boxes - truck_boxes_count
jars_diff = jars - (truck_boxes_count * truck_jar_count)

print('Total lutenica: {0:.0f} kilograms.'.format(math.floor(total_kg_lutenitsa)))
if boxes >= truck_boxes_count:
    print('{0:.0f} boxes left.'.format(math.floor(boxes_diff)))
    print('{0:.0f} jars left.'.format(math.floor(jars_diff)))
else:
    print('{0:.0f} more boxes needed.'.format(math.floor(boxes_diff * -1)))
    print('{0:.0f} more jars needed.'.format(math.floor(jars_diff * -1)))
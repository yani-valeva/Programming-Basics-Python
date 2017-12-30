import math
days_count = int(input())
food_kg = int(input())
first_deer_food = float(input())
second_deer_food = float(input())
third_deer_food = float(input())

first_deer = days_count * first_deer_food
second_deer = days_count * second_deer_food
third_deer = days_count * third_deer_food
food = first_deer + second_deer + third_deer

if food <= food_kg:
    print('{0} kilos of food left.'.format(math.floor(food_kg - food)))
else:
    print('{0} more kilos of food are needed.'.format(math.ceil(food - food_kg)))
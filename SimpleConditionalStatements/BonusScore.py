number = int(input())
bonus_score = 0.0
add_bonus_score = 0.0

if number <= 100:
    bonus_score = 5
elif number <= 1000:
    bonus_score = 0.2 * number
elif number > 1000:
    bonus_score = 0.1 * number

if number % 2 == 0:
    add_bonus_score = 1

if number % 10 == 5:
    add_bonus_score = 2

total_bonus_score = bonus_score + add_bonus_score
number_with_bonus = number + total_bonus_score

print(total_bonus_score)
print(number_with_bonus)
first_number = int(input())
second_number = int(input())

max_number = max(first_number, second_number)
min_number = min(first_number, second_number)

while min_number != 0:
    reminder = max_number % min_number
    max_number = min_number
    min_number = reminder
print(max_number)

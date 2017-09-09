number = int(input())
first_number = 1
second_number = 1

if number == 1 or number == 2:
    print(1)
    quit()

temporary = 0

for i in range(3, number + 1):
    if i % 2 != 0:
        temporary = first_number + second_number
        first_number = second_number
        second_number = temporary
    else:
        temporary = second_number * (i // 2)
        first_number = second_number
        second_number = temporary

print(second_number)
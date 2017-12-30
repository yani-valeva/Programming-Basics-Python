first_number = int(input())
second_number = int(input())
first_start = 0
first_end = 0
second_start = 0
second_end = 0
third_start = 0
third_end = 0
fourth_start = 0
fourth_end = 0

for i in range(0, 4):
    if i == 0:
        fourth_start = first_number % 10
        fourth_end = second_number % 10
        first_number = first_number // 10
        second_number = second_number // 10
    elif i == 1:
        third_start = first_number % 10
        third_end = second_number % 10
        first_number = first_number // 10
        second_number = second_number // 10
    elif i == 2:
        second_start = first_number % 10
        second_end = second_number % 10
        first_number = first_number // 10
        second_number = second_number // 10
    elif i == 3:
        first_start = first_number % 10
        first_end = second_number % 10
        first_number = first_number // 10
        second_number = second_number // 10

for a in range(first_start, first_end + 1):
    for b in range (second_start, second_end + 1):
        for c in range (third_start, third_end + 1):
            for d in range (fourth_start, fourth_end + 1):
                if(a % 2 != 0 and b % 2 != 0 and c % 2 != 0 and d % 2 != 0):
                    print('{0}{1}{2}{3}'.format(a, b, c, d), end=" ")
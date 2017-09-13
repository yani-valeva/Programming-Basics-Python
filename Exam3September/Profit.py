count_one = int(input())
count_two = int(input())
count_five = int(input())
sum = int(input())

for i in range(0, count_one + 1):
    for j in range(0, count_two + 1):
        for k in range(0, count_five + 1):
            if i + (j * 2) + (k * 5) == sum:
                print("{0} * 1 lv. + {1} * 2 lv. + {2} * 5 lv. = {3} lv.".format(i, j, k, sum))
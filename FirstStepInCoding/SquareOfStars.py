number= int(input())

for row in range(1, number + 1):
    if row == 1 or row == number:
        print('*' * number)

    else:
        print('*' + ' ' * (number - 2) + '*')

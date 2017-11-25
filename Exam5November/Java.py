number = int(input())

for i in range(0, number):
    print(' ' * (number - 1) + ' ~' * 3)

print('=' * (3 * number + 5))

for i in range(0, number - 2):
    if(i == number // 2 - 1):
        print('|' + '~' * number + 'JAVA' + '~' * number + '|' + ' ' * (number - 1) + '|')
    else:
        print('|' + '~' * (2 * number + 4) + '|' + ' ' * (number - 1) + '|')

print('=' * (3 * number + 5))

monkey = (2 * number + 4)
space = 0

for i in range(0, number):
    print(' ' * space + '\\' + '@' * monkey + '/')
    monkey -= 2
    space += 1

print('=' * (2 * number + 6))
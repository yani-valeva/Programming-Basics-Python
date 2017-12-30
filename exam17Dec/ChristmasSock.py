n = int(input())

dash = 2 * n

print('|' + '-' * dash + '|')
print('|' + '*' * dash + '|')
print('|' + '-' * dash + '|')

dash = ((2 * n) - 2) // 2
tilda = 2

for i in range(1, n):
    print('|' + '-' * dash + '~' * tilda + '-' * dash + '|')
    dash -= 1
    tilda += 2

dash += 2
tilda -= 4

for i in range(1, n - 1):
    print('|' + '-' * dash + '~' * tilda + '-' * dash + '|')
    dash += 1
    tilda -= 2

dash = 0
dots = (2 * n) + 1

for i in range(0, n // 2):
    print('-' * dash + '\\' + '.' * dots + '\\')
    dash += 1

dots_second = (dots - 5) // 2

print('-' * dash + '\\' + '.' * dots_second + 'MERRY' + '.' * dots_second + '\\')
dash += 1

print('-' * dash + '\\' + '.' * dots + '\\')
dash += 1

print('-' * dash + '\\' + '.' * dots_second + 'X-MAS' + '.' * dots_second + '\\')
dash += 1

if n % 2 == 0:
    for i in range(0, (n // 2) - 1):
        print('-' * dash + '\\' + '.' * dots + '\\')
        dash += 1
else:
    for i in range(0, n // 2):
        print('-' * dash + '\\' + '.' * dots + '\\')
        dash += 1

print('-' * dash + '\\' + '_' * dots + ')')
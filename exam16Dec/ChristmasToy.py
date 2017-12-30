n = int(input())
dash = 2 * n
sign = n
star = 1

print('-' * dash + '*' * sign + '-' * dash)
dash -= 2
sign += 2
for i in range(0, n // 2 ):
    print('-' * dash + '*' * star + '&' * sign + '*' * star + '-' * dash)
    dash -= 2
    sign += 2
    star += 1

dash += 1
star = 2
sign = (5 * n) - ((dash * 2) + 4)

for i in range (0, n // 2):
    print('-' * dash + '**' + '~' * sign + '**' + '-' * dash)
    dash -= 1
    sign += 2

dash += 1
sign = (5 * n) - ((dash * 2) + 2)

print('-' * dash + '*' + '|' * sign + '*' + '-' * dash)

sign -= 2

for i in range (0, n // 2):
    print('-' * dash + '**' + '~' * sign + '**' + '-' * dash)
    dash += 1
    sign -= 2

star = n // 2
sign = (5 * n) - ((dash * 2) + (star * 2))

for i in range (0, n // 2):
    print('-' * dash + '*' * star + '&' * sign + '*' * star + '-' * dash)
    dash += 2
    sign -= 2
    star -= 1

dash = n * 2
sign = n

print('-' * dash + '*' * sign + '-' * dash)
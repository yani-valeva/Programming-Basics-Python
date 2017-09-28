number = int(input())

dots = ((3 * number) - 1) // 2
print('.' * dots + 'x' + '.' * dots)
print('.' * (dots - 1) + '/' + 'x' + '\\' + '.' * (dots - 1))
print('.' * (dots - 1) + 'x' + '|' + 'x' + '.' * (dots - 1))

ex = number
dots = ((3 * number) - ((ex * 2) + 1)) // 2
for i in range(1, (number // 2) + 2):
    print('.' * dots + 'x' * ex + '|' + 'x' * ex + '.' * dots)
    dots = dots - 1
    ex = ex + 1
ex = ex - 2
dots = dots + 2
for a in range(1, (number // 2) + 1):
    print('.' * dots + 'x' * ex + '|' + 'x' * ex + '.' * dots)
    dots = dots + 1
    ex = ex - 1

dots = ((3 * number) - 1) // 2
print('.' * (dots - 1) + '/' + 'x' + '\\' + '.' * (dots - 1))
print('.' * (dots - 1) + '\\' + 'x' + '/' + '.' * (dots - 1))
ex = number
dots = ((3 * number) - ((ex * 2) + 1)) // 2
for i in range(1, (number // 2) + 2):
    print('.' * dots + 'x' * ex + '|' + 'x' * ex + '.' * dots)
    dots = dots - 1
    ex = ex + 1
ex = ex - 2
dots = dots + 2
for a in range(1, (number // 2) + 1):
    print('.' * dots + 'x' * ex + '|' + 'x' * ex + '.' * dots)
    dots = dots + 1
    ex = ex - 1
dots = ((3 * number) - 1) // 2
print('.' * (dots - 1) + 'x' + '|' + 'x' + '.' * (dots - 1))
print('.' * (dots - 1) + '\\' + 'x' + '/' + '.' * (dots - 1))
print('.' * dots + 'x' + '.' * dots)
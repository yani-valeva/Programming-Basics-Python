number = int(input())
inner_dots = number
outer_dots = 0

for i in range(1, number):
    print('.' * outer_dots + '*' + '.' * inner_dots + '*' + '.' * inner_dots + '*' + '.' * outer_dots)
    inner_dots -= 1
    outer_dots += 1
print('.' * outer_dots + "*****" + '.' * outer_dots)
print('*' * ((2 * number) + 3))
print('.' * outer_dots + "*****" + '.' * outer_dots)

inner_dots += 1
outer_dots -= 1

for i in range(1, number):
    print('.' * outer_dots + '*' + '.' * inner_dots + '*' + '.' * inner_dots + '*' + '.' * outer_dots)
    inner_dots += 1
    outer_dots -= 1

n = int(input())
third = n % 10
first = n // 100
second = n // 10 % 10

for a in range(1, third + 1):
    for b in range(1, second + 1):
        for c in range(1, first + 1):
            print('{0} * {1} * {2} = {3};'.format(a, b, c, (a * b * c)))
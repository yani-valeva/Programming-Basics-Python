# first option

n = int(input())
k = int(input())

first_result = (5 ** n) * (2 ** k)
second_result = (5 ** (k // n)) * (2 ** (n % k))
result = first_result / second_result
print('{0:.10f}'.format(result))

# second option

import math
n = int(input())
k = int(input())

first_result = math.pow(5, n) * math.pow(2, k)
second_result = math.pow(5, (k // n)) * math.pow(2, (n % k))
result = first_result / second_result
print('{0:.10f}'.format(result))
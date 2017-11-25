import math
number = int(input())

if number < 2:
    print("Not Prime")
    quit()

for i in range(2, math.floor(math.sqrt(number)) + 1):
    if number % i == 0:
        print("Not Prime")
        quit()

print("Prime")
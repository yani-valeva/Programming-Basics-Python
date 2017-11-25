number = int(input())

for i in range(1, number + 1):
    increase = i
    decrease = number - 1
    for j in range(1, number + 1):

        if increase <= number:
            print(increase, end=" ")
            increase += 1
        else:
            print(decrease, end=" ")
            decrease -= 1

    print()
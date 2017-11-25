number = int(input())
count = 1

for i in range(1, number + 1):
    for j in range(1, i + 1):
        print(count, end=" ")

        if count == number:
            quit()

        count += 1

    print()

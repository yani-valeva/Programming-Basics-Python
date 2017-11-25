number = int(input())
first_fibonacci = 1
second_fibonacci = 1

for i in range(2, number + 1):
    temporary = first_fibonacci
    first_fibonacci = second_fibonacci
    second_fibonacci = temporary + second_fibonacci

print(second_fibonacci)
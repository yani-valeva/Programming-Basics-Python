number = int(input("Еnter a number in the range [1...100]: "))

while not (1 <= number <= 100):
    print("Invalid number!")
    number = int(input("Еnter a number in the range [1...100]: "))

print("The number is: {0}".format(number))
while 1:
    try:
        number = int(input("Enter even number: "))
        if number % 2 == 0:
            print("Even number entered: {0}".format(number))
            quit()
        else:
            print("The number is not even.")
    except ValueError:
        print("Invalid number!")



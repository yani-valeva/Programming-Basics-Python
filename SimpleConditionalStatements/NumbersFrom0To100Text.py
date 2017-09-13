number = int(input())
first_number = number // 10
second_number = number % 10
both_number = number
first_word = ""
second_word = ""
both_word = ""
if second_number == 0:
    second_word = "zero"
elif second_number == 1:
    second_word = "one"
elif second_number == 2:
    second_word = "two"
elif second_number == 3:
    second_word = "three"
elif second_number == 4:
    second_word = "four"
elif second_number == 5:
    second_word = "five"
elif second_number == 6:
    second_word = "six"
elif second_number == 7:
    second_word = "seven"
elif second_number == 8:
    second_word = "eight"
elif second_number == 9:
    second_word = "nine"

if first_number == 2:
    first_word = "twenty"
elif first_number == 3:
    first_word = "thirty"
elif first_number == 4:
    first_word = "forty"
elif first_number == 5:
    first_word = "fifty"
elif first_number == 6:
    first_word = "sixty"
elif first_number == 7:
    first_word = "seventy"
elif first_number == 8:
    first_word = "eighty"
elif first_number == 9:
    first_word = "ninety"

if both_number == 10:
    both_word = "ten"
elif both_number == 11:
    both_word = "eleven"
elif both_number == 12:
    both_word = "twelve"
elif both_number == 13:
    both_word = "thirteen"
elif both_number == 14:
    both_word = "fourteen"
elif both_number == 15:
    both_word = "fifteen"
elif both_number == 16:
    both_word = "sixteen"
elif both_number == 17:
    both_word = "seventeen"
elif both_number == 18:
    both_word = "eighteen"
elif both_number == 19:
    both_word = "nineteen"

if number >= 0 and number <= 9:
    print(second_word)
elif number >= 10 and number <= 19:
    print(both_word)
elif number >= 20 and number <= 100:
    if number % 10 == 0 and number != 100:
        print(first_word)
    elif number == 100:
        print("one hundred")
    else:
        print("{0} {1}".format(first_word, second_word))
else:
    print("invalid number")
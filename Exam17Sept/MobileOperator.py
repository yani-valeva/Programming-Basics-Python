contract_term = input()
contract_type = input()
internet = input()
months = int(input())
sum = 0.0
if contract_term == "one":
    if contract_type == "Small":
       sum = 9.98
    elif contract_type == "Middle":
        sum = 18.99
    elif contract_type == "Large":
        sum = 25.98
    elif contract_type == "ExtraLarge":
        sum = 35.99
elif contract_term == "two":
    if contract_type == "Small":
        sum = 8.58
    elif contract_type == "Middle":
        sum = 17.09
    elif contract_type == "Large":
        sum = 23.59
    elif contract_type == "ExtraLarge":
        sum = 31.79

if internet == "yes":
    if sum <= 10:
        sum = sum + 5.50
    elif sum <= 30:
        sum = sum + 4.35
    else:
        sum = sum + 3.85

if contract_term == "two":
    sum = sum - (sum * 0.0375)

total_sum = sum * months
print('{0:.2f} lv.'.format(total_sum))
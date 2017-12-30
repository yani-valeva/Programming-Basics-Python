budget = float(input())
first_kid = float(input())
second_kid = float(input())
third_kid = float(input())

total_sum = first_kid + second_kid + third_kid
total_sum = budget - total_sum
total_sum -= total_sum * 0.1

print('{0:.2f}'.format(total_sum))
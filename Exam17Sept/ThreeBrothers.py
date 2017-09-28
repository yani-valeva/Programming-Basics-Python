import math
first_brother_time = float(input())
second_brother_time = float(input())
third_brother_time = float(input())
fishing_time = float(input())

time = 1 / ((1 / first_brother_time) + (1 / second_brother_time) + (1 / third_brother_time))
total_time = time + (time * 0.15)
result_time = 0.0
print('Cleaning time: {0:.2f}'.format(total_time))
if  fishing_time - total_time > 0:
    result_time = math.floor(fishing_time - total_time)
    print('Yes, there is a surprise - time left -> {0} hours.'.format(result_time))
else:
    result_time = math.ceil(total_time - fishing_time)
    print('No, there isn\'t a surprise - shortage of time -> {0} hours.'.format(result_time))
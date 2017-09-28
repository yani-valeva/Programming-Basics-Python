length = int(input())
width = int(input())
height = int(input())
number = float(input())

volume = length * width * height
total_liters = volume * 0.001
percent = number * 0.01
result = total_liters * (1 - percent)

print('{0:.3f}'.format(result))
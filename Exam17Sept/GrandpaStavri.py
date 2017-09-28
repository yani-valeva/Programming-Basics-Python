days = int(input())
liters = 0.0
total_degrees = 0.0
for i in range(0, days):
    rakiaQuantity = float(input())
    degrees = float(input())
    liters = liters + rakiaQuantity
    total_degrees = total_degrees + (rakiaQuantity * degrees)
result_degrees = total_degrees / liters
print('Liter: {0:.2f}'.format(liters))
print('Degrees: {0:.2f}'.format(result_degrees))

if result_degrees < 38:
    print('Not good, you should baking!')
elif result_degrees >= 38 and result_degrees <= 42:
    print('Super!')
else:
    print('Dilution with distilled water!')
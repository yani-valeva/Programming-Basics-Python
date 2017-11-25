weight = float(input())
service_type = input()
distance = int(input())
price = 0.0

if service_type == "standard":
    if weight < 1:
        price = 0.03 * distance
    elif weight <= 10:
        price = 0.05 * distance
    elif weight <= 40:
        price = 0.10 * distance
    elif weight <= 90:
        price = 0.15 * distance
    else:
        price = 0.20 * distance
elif service_type == "express":
    if weight < 1:
        price = (0.03 * distance) + ((0.8 * 0.03) * weight * distance)
    elif weight <= 10:
        price = (0.05 * distance) + ((0.4 * 0.05) * weight * distance)
    elif weight <= 40:
        price = (0.10 * distance) + ((0.05 * 0.10) * weight * distance)
    elif weight <= 90:
        price = (0.15 * distance) + ((0.02 * 0.15) * weight * distance)
    else:
        price = (0.20 * distance) + ((0.01 * 0.20) * weight * distance)

print('The delivery of your shipment with weight of {0:.3f} kg. would cost {1:.2f} lv.'.format(weight, price))
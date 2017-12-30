nights_count = int(input())
destination = input()
transport = input()
price = 0.0
transport_price = 0.0

if destination == "Miami":
    if nights_count > 15:
        price = ((2 * 20) + (3 * 10)) * nights_count
        price += price * 0.25
    elif nights_count > 10:
        price = ((2 * 22.99) + (3 * 11.99)) * nights_count
        price += price * 0.25
    else:
        price = ((2 * 24.99) + (3 * 14.99)) * nights_count
        price += price * 0.25
elif destination == "Canary Islands":
    if nights_count > 15:
        price = ((2 * 28) + (3 * 22)) * nights_count
        price += price * 0.25
    elif nights_count > 10:
        price = ((2 * 30.50) + (3 * 25.60)) * nights_count
        price += price * 0.25
    else:
        price = ((2 * 32.50) + (3 * 28.50)) * nights_count
        price += price * 0.25
elif destination == "Philippines":
    if nights_count > 15:
        price = ((2 * 38.50) + (3 * 32.40)) * nights_count
        price += price * 0.25
    elif nights_count > 10:
        price = ((2 * 41) + (3 * 36)) * nights_count
        price += price * 0.25
    else:
        price = ((2 * 42.99) + (3 * 39.99)) * nights_count
        price += price * 0.25

if transport == "train":
    transport_price = (2 * 22.30) + (3 * 12.50)
elif transport == "bus":
    transport_price = (2 * 45) + (3 * 37)
elif transport == "airplane":
    transport_price = (2 * 90) + (3 * 68.50)

price += transport_price

print('{0:.3f}'.format(price))
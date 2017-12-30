days = int(input()) - 1
room_type = input()
mark = input()
price = 0.0

if room_type == "apartment":
    price = days * 25
    if days > 15:
        price -= price * 0.5
    elif days >= 10:
        price -= price * 0.35
    else:
        price -= price * 0.3
elif room_type == "president apartment":
    price = days * 35
    if days > 15:
        price -= price * 0.2
    elif days >= 10:
        price -= price * 0.15
    else:
        price -= price * 0.1
elif room_type == "room for one person":
    price = days * 18

if mark == "positive":
    price += price * 0.25
elif mark == "negative":
    price -= price * 0.1

print('%.2f' % price)

pictures_count = int(input())
picture_type = input()
order_type = input()
price = 0.0
if picture_type == "9X13":
    price = pictures_count * 0.16
    if pictures_count > 50:
        price -= price * 0.05
elif picture_type == "10X15":
    price = pictures_count * 0.16
    if pictures_count > 80:
        price -= price * 0.03
elif picture_type == "13X18":
    price = pictures_count * 0.38
    if pictures_count >= 50 and pictures_count <= 100:
        price -= price * 0.03
    elif pictures_count > 100:
        price -= price * 0.05
elif picture_type == "20X30":
    price = pictures_count * 2.90
    if pictures_count >= 10 and pictures_count <= 50:
        price -= price * 0.07
    elif pictures_count > 50:
        price -= price * 0.09

if order_type == "online":
    price -= price * 0.02
print('{0:.2f}BGN'.format(price))
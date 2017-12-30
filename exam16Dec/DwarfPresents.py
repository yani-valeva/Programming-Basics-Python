elf_count = int(input())
price = int(input())
total_price = 0.0

for i in range(0, elf_count):
    gift = input()
    if gift == "sand clock":
        total_price += 2.2
    elif gift == "magnet":
        total_price += 1.5
    elif gift == "cup":
        total_price += 5
    elif gift == "t-shirt":
        total_price += 10

if total_price <= price:
    print('Santa Claus has {0:.2f} more leva left!'.format(price - total_price))
else:
    print('Santa Claus will need {0:.2f} more leva.'.format(total_price - price))
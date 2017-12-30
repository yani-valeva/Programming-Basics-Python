paper_rolls = int(input())
cloth_rolls = int(input())
glue_litters = float(input())
percent = int(input())

paper_price = paper_rolls * 5.80
cloth_price = cloth_rolls * 7.20
glue_price = glue_litters * 1.20
total_price = paper_price + cloth_price + glue_price
total_price -= total_price * (percent / 100)
print('{0:.3f}'.format(total_price))
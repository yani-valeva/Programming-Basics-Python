table = int(input())
length = float(input())
width = float(input())
cover_area = table * (length + 2 * 0.30) * (width + 2 * 0.30)
box_area = table * (length / 2) * (length / 2)
price_usd = (cover_area * 7) + (box_area * 9)
price_bgn = price_usd * 1.85
print('{0:.2f} USD'.format(price_usd))
print('{0:.2f} BGN'.format(price_bgn))
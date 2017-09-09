size = int(input())
y = int(input())
x = int(input())

if (-3 * size < x < 3 * size and -2 * size < y < -size) or (-2 * size <= x <= 2 * size and size > y > -size) or (-3 * size < x < 3 * size and 2 * size > y > size) or (y == size and -2 * size < x < 2 * size) or (y == -size and -2 * size < x < 2 * size):
    print("INSIDE")
elif (y == -2 * size and -3 * size <= x <= 3 * size) or ((x == -3 * size or x == 3 * size) and -2 * size <= y <= -size) or ((y == -size) and (-3 * size <= x <= -2 * size or 2 * size <= x <= 3 * size)) or ((x == -2 * size or x == 2 * size) and size >= y >= -size) or ((y == size) and (-3 * size <= x <= -2 * size or 2 * size <= x <= 3 * size)) or ((x == -3 * size or x == 3 * size) and size <= y <= 2 * size) or (y == 2 * size and -3 * size <= x <= 3 * size):
    print("BORDER")
else:
    print("OUTSIDE")
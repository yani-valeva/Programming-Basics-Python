x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

a = max(x1, x2) - min(x1, x2)
b = max(y1, y2) - min(y1, y2)
area = a * b
perimeter = 2 * (a + b)

print(area)
print(perimeter)
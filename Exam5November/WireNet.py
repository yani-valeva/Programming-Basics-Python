place_length = int(input())
place_width = int(input())
fence_height = float(input())
fence_price_per_meter = float(input())
fence_weight_per_sq_meter = float(input())

fence_length = (2 * place_length) + (2 * place_width)
total_price = fence_length * fence_price_per_meter
fence_area = fence_length * fence_height
total_weight = fence_area * fence_weight_per_sq_meter

print(fence_length)
print('{0:.2f}'.format(total_price))
print('{0:.3f}'.format(total_weight))
number = input()

lst = []
count = 1

for i in range(0, len(number)):
    lst.append(number[len(number) - count])
    count += 1

lst = ''.join(lst)
result = number + ''.join(lst)

result = result.strip('0')
print(result)


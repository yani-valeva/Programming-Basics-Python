size = int(input())
hours = int(input())
question = 1
current_size = size
current_hour = hours

if hours == 0:
    print('*' + ' *' * (current_size - 1))
else:
    print('-' + ' -' * (current_size - 1))

for i in range(1, current_hour):
    current_size = current_size - 1
    if i % 2 == 1:
        print('?' * question + '- ' * (current_size - 1) + '-' + '?' * question)

    else:
        print(' ' * question + '- ' * (current_size - 1) + '-' + ' ' * question)
    question = question + 1

current_size = current_size - 1
is_even = True
if hours % 2 == 0:
    is_even = False
if hours == 0:
    is_even = True
sec_size = size - (hours + 1)

for i in range(1, sec_size + 1):
    if is_even == True:
        print('?' * question + '* ' * (current_size - 1)  + '*' + '?' * question)
        is_even = False
    else:
        print(' ' * question + '* ' * (current_size - 1) + '*' + ' ' * question)
        is_even = True
    if hours == 0 and i == sec_size - 1:
        current_size = current_size - 1
        question = question + 1
        break
    current_size = current_size - 1
    question = question + 1

if is_even == True:
    print('?' * question + 'o' + '?' * question)
    is_even = False
else:
    print(' ' * question + 'o' + ' ' * question)
    is_even = True

current_size = current_size + 1
question = question - 1

for i in range(1, sec_size + 1):
    if is_even == True:
        print('?' * question + '- ' * (current_size - 1) + '-' + '?' * question)
        is_even = False
    else:
        print(' ' * question + '- ' * (current_size - 1) + '-' + ' ' * question)
        is_even = True
    if hours == 0 and i == sec_size - 1:
        current_size = current_size + 1
        question = question - 1
        break
    current_size = current_size + 1
    question = question - 1

for i in range(1, current_hour):
    if is_even == True:
        print('?' * question + '* ' * (current_size - 1) + '*' + '?' * question)
        is_even = False
    else:
        print(' ' * question + '* ' * (current_size - 1) + '*' + ' ' * question)
        is_even = True
    current_size = current_size + 1
    question = question - 1

if hours == 0:
    print('-' + ' -' * (current_size - 1))
else:
    print('*' + ' *' * (current_size - 1))
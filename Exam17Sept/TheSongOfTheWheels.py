number = int(input())
is_found = False
has_password = False
count = 0
password = ""

for a in range(1, 9 + 1):
    for b in range(1, 9 + 1):
        for c in range(1, 9 + 1):
            for d in range(1, 9 + 1):
                if a < b and c > d:
                    if (a * b) + (c * d) == number:
                        print('{0}{1}{2}{3}'.format(a, b, c, d),end=" ")
                        is_found = True
                        count = count + 1
                        if count == 4:
                            password = '{0}{1}{2}{3}'.format(a, b, c, d)
                            has_password = True
print()
if is_found == False:
    print('No!')
    exit()
elif is_found == True and has_password == True:
    print('Password: {0}'.format(password))
    exit()

if has_password == False:
    print('No!')

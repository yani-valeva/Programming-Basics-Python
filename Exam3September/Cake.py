width = int(input())
length = int(input())
pieces_str = input()
area = width * length
while (pieces_str != "STOP"):
    pieces = int(pieces_str)
    if area < pieces:
        print('No more cake left! You need {0} pieces more.'.format(pieces - area))
        exit()
    area -= pieces
    pieces_str = input()
print('{0} pieces are left.'.format(area))
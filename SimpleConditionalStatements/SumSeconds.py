first_sportsman = int(input())
second_sportsman = int(input())
third_sportsman = int(input())

sumSeconds = first_sportsman + second_sportsman + third_sportsman
minutes = sumSeconds // 60
seconds = sumSeconds % 60

print('{0:}:{1:02d}' .format(minutes, seconds))
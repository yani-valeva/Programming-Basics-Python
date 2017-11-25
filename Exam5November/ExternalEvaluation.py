students_count = int(input())
poor = 0
satisfactory = 0
good = 0
very_good = 0
excellent = 0
for i in range(0, students_count):
    points = int(input())
    if points <= 22.5:
        poor += 1
    elif points <= 40.5:
        satisfactory += 1
    elif points <= 58.5:
        good += 1
    elif points <= 76.5:
        very_good += 1
    else:
        excellent += 1

poor_percentage = poor * 100.0 / students_count
satisfactory_percentage = satisfactory * 100.0 / students_count
good_percentage = good * 100.0 / students_count
very_good_percentage = very_good * 100.0 / students_count
excellent_percentage = excellent * 100.0 / students_count

print('{0:.2f}% poor marks'.format(poor_percentage))
print('{0:.2f}% satisfactory marks'.format(satisfactory_percentage))
print('{0:.2f}% good marks'.format(good_percentage))
print('{0:.2f}% very good marks'.format(very_good_percentage))
print('{0:.2f}% excellent marks'.format(excellent_percentage))
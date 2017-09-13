import math
income = float(input())
average_grades = float(input())
min_salary = float(input())
social_scholarship = 0.35 * min_salary
scholarship = average_grades * 25
has_social_scholarship = False
has_scholarship = False
if income < min_salary and average_grades > 4.5:
    has_social_scholarship = True
if average_grades >= 5.5:
    has_scholarship = True
if has_social_scholarship == False and has_scholarship == False:
    print("You cannot get a scholarship!")
    exit()
if has_social_scholarship and has_scholarship and social_scholarship > scholarship:
    result = math.floor(social_scholarship)
    print('You get a Social scholarship {0} BGN'.format(result))
    exit()
if has_social_scholarship and has_scholarship and social_scholarship <= scholarship:
    result = math.floor(scholarship)
    print('You get a scholarship for excellent results {0} BGN'.format(result))
    exit()
if has_social_scholarship:
    result = math.floor(social_scholarship)
    print('You get a Social scholarship {0} BGN'.format(result))
    exit()
if has_scholarship:
    result = math.floor(scholarship)
    print('You get a scholarship for excellent results {0} BGN'.format(result))

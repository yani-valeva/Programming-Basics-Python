guests_count = int(input())
budget = int(input())
total_price = guests_count * 20
fireworks = 0
donation = 0

if total_price <= budget:
    total_price = budget - total_price
    fireworks = 0.4 * total_price
    donation = total_price - fireworks
    print('Yes! {0} lv are for fireworks and {1} lv are for donation.'.format(round(fireworks), round(donation)))
else:
    print('They won’t have enough money to pay the covert. They will need {0} lv more.'.format(round(total_price - budget)))
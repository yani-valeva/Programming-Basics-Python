money = float(input())
inputCurrency = input()
outputCurrency = input()
bgn = 0
eur = 0
gbp = 0
usd = 0

if inputCurrency == 'USD':
    usd = money
    bgn = money * 1.79549
    eur = bgn / 1.95583
    gbp = bgn / 2.53405
elif inputCurrency == 'BGN':
    bgn = money
    usd = money / 1.79549
    eur = money / 1.95583
    gbp = money / 2.53405
elif inputCurrency == 'EUR':
    eur = money
    bgn = money * 1.95583
    usd = bgn / 1.79549
    gbp = bgn / 2.53405
elif inputCurrency == 'GBP':
    gbp = money
    bgn = money * 2.53405
    usd = bgn / 1.79549
    eur = bgn / 1.95583

if outputCurrency == 'BGN':
    print('{0} BGN'.format(round(bgn, 2)))
elif outputCurrency == 'USD':
    print('{0} USD'.format(round(usd, 2)))
elif outputCurrency == 'EUR':
     print('{0} EUR'.format(round(eur, 2)))
elif outputCurrency == 'GBP':
    print('{0} GBP'.format(round(gbp, 2)))
def invest(amount, rate, years):
    for year in range(1, years + 1):
        amount = amount * (1 + rate)
        print(f'year {year}: ${amount:,.2f}')


amount = float(input('Enter your investment amount: '))
rate = float(input('Enter a rate: ' ))
years = int(input('Enter the length of the investment: '))

invest(amount, rate, years)


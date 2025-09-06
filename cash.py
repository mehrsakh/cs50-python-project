import cs50

while True:
    dollars = cs50.get_float('Change owed: ')
    if dollars > 0:
        cents = round(dollars * 100)
        coins = 0

        quarters = int(cents / 25)

        dime = int((cents % 25) / 10)

        nickels = int(((cents % 25) % 10) / 5)

        pennies = int(((cents % 25) % 10) % 5)

        # Don't overthink it, if the cents is less than 25, the coins of quarters is zero
        coins = coins + quarters
        if dime > 0:
            coins = coins + dime
        if nickels > 0:
            coins = coins + nickels
        if pennies > 0:
            coins = coins + pennies

        print(coins)
        break

def atm():
    correct_pin = 3030

    pin = int(input('Please enter pin:' ))

    try:
        count = 0
        while count < 2:
            if pin == correct_pin:
                break

            count += 1
            pin = int(input(f'Wrong pin, try again. You have {3 - count} entries left'))

        if pin == correct_pin:
            balance = 100
            amount = int(input('Please enter the amount of money you want to withdraw:' ))

            if amount < balance:
                balance = balance - amount
                print(f'Successful! Your balance is: {balance}')
            else:
                raise Exception('Error! insufficient funds.')

        else:

            raise Exception('You have tried more than 3 times. Your card has been swallowed')

    except Exception as e:
        raise Exception(e)


atm()

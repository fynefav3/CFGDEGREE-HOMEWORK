def pin_validation(pin):
    correct_pin = 3030
    correct = pin == correct_pin
    if not correct:
        raise ValueError("Incorrect pin, Please try again")

def pin_validation_1(pin):
    if len(pin) >4:
        raise ValueError("Pin should be 4 digits")




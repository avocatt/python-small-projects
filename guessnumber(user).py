import random


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could be high also
        guess = random.randint(low, high)
        feedback = input(
            'Is {} too high (H), too low (L) or correct (C)? '.format(guess)).lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print('computer guessed your number, {} correctly.'.format(guess))


computer_guess(10)

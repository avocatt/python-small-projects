import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input('Guess a number between 1 and {}:'.format(x)))
        if guess < random_number:
            print('sorry, guess again. too low')
        elif guess > random_number:
            print('sorry, guess again. too high')

    print('congratz, you have guessed the number {}'.format(random_number))


guess(10)

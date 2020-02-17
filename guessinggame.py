import random
import sys


class GuessNumber:

    def __init__(self):
        self.secret_number = random.randint(1, 20)

    def main(self):
        guess = int(input('Guess a number between 1 and 20.'))

        if guess > self.secret_number:
            print('Your guess is too high.')
        elif guess < self.secret_number:
            print('Your guess is too low.')
        elif guess == self.secret_number:
            print('That\'s it!')
            sys.exit()

    def guesses_taken(self):
        guesses_taken = 0

        while guesses_taken < 6:
            guesses_taken += 1
            self.main()
            if guesses_taken == 6:
                print('I\'m sorry, the correct answer was ' + str(self.secret_number) + '.')
                break


game_1 = GuessNumber()
game_1.guesses_taken()

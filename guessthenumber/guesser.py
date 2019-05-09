from guessthenumber.common import (
    generate_stringified_random_number,
    max_cipher_quantity_number,
)


class Guesser:

    def __init__(self, cipher_quantity):
        self.lower_guess = 0
        self.current_guess = None
        self.higher_guess = max_cipher_quantity_number(cipher_quantity)

    def take_a_guess(self, hint=None):
        if hint is None:
            guess =  self.higher_guess // 2
            self.current_guess = guess
            return guess

        if hint == 'lower':
            guess = (self.lower_guess + self.current_guess) // 2
            self.higher_guess, self.current_guess = self.current_guess, guess
            return guess

        if hint == 'higher':
            guess = (self.current_guess + self.higher_guess) // 2
            self.lower_guess, self.current_guess = self.current_guess, guess
            return guess

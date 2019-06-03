from typing import Optional

from guessthenumber.common import max_cipher_quantity_number


class Guesser:

    def __init__(self, cipher_quantity: int) -> None:
        self.lower_guess: int = 0
        self.current_guess: int = 0
        self.higher_guess: int = max_cipher_quantity_number(cipher_quantity)

    def take_a_guess(self, hint: Optional[str] = None) -> Optional[str]:

        guess: Optional[int] = None

        if hint is None:
            guess = self.higher_guess // 2
            self.current_guess = guess
        elif hint == 'lower':
            guess = (self.lower_guess + self.current_guess) // 2
            self.higher_guess, self.current_guess = self.current_guess, guess
        elif hint == 'higher':
            guess = (self.current_guess + self.higher_guess) // 2
            self.lower_guess, self.current_guess = self.current_guess, guess

        return str(guess) if guess else None

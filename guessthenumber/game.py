from abc import (
    ABC,
    abstractmethod,
)

from guessthenumber.constants import GAME_OVER_MESSAGE
from guessthenumber.evaluator import (
    Answer,
    Evaluator,
)
from guessthenumber.guesser import Guesser
from guessthenumber.thinker import Thinker


class Game(ABC):

    @abstractmethod
    def play(self, cipher_quantity: int = 4, additional_message: str = None) -> None:
        raise NotImplementedError('Must implement a subclass.')


class MachineGuessesHumanThinksGame(Game):

    def play(self, cipher_quantity: int = 4, additional_message: str = None) -> None:

        guesser: Guesser = Guesser(cipher_quantity)
        hint: str = ''

        while True:
            guess: str = guesser.take_a_guess(hint)

            if guess is None:
                break

            hint = input('My guess: {guess}. If not right, please give a hint:\n--> '.format(guess=guess))

        print(GAME_OVER_MESSAGE)


class HumanGuessesMachineThinksGame(Game):

    # TODO: cipher_quantity is not used because at some point the machine
    # should ask how many ciphers are going to be used to play.
    def play(self, cipher_quantity: int = 4, additional_message: str = None) -> None:
        number: str = Thinker.think_number(cipher_quantity=4)

        while True:
            guess: str = self.ask_for_a_guess(additional_message)
            answer: Answer = Evaluator.evaluate_guess(guess, number)

            if answer:
                break

            additional_message = str(answer)

        print(GAME_OVER_MESSAGE)

    @staticmethod
    def ask_for_a_guess(additional_message: str = None) -> str:
        if additional_message:
            print(additional_message)

        return input('Please, take a guess: ')


if __name__ == '__main__':
    which_game: str = input(
        'Hey there! There are two games to play here:\n\t'
        '1. Machine guesses, you think\n\t'
        '2. You guess, machine thinks\n'
        '-->  '
    )
    if int(which_game) == 1:
        game: Game = MachineGuessesHumanThinksGame()
    else:
        game = HumanGuessesMachineThinksGame()

    game.play()

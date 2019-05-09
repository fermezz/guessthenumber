from guessthenumber.constants import GAME_OVER_MESSAGE
from guessthenumber.thinker import Thinker
from guessthenumber.evaluator import Evaluator


class Game:

    def play(self, additional_message=None):
        number = Thinker.think_number(cipher_quantity=4)
        additional_message = None

        while True:
            guess = self.ask_for_a_guess(additional_message)
            answer = Evaluator.evaluate_guess(guess, number)

            if answer:
                break

            additional_message = str(answer)

        print(GAME_OVER_MESSAGE)


    def ask_for_a_guess(self, additional_message=None):
        if additional_message:
            print(additional_message)

        return input("Please, take a guess: ")


if __name__ == "__main__":
    game = Game()
    game.play()

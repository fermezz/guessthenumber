from mock import patch

from guessthenumber.constants import GAME_OVER_MESSAGE
from guessthenumber.evaluator import (
    Answer,
    Evaluator,
)
from guessthenumber.game import (
    HumanGuessesMachineThinksGame,
    MachineGuessesHumanThinksGame,
)
from guessthenumber.guesser import Guesser
from guessthenumber.thinker import Thinker


class TestGames:

    @patch('guessthenumber.evaluator.Evaluator.evaluate_guess', return_value=True)
    @patch('guessthenumber.game.HumanGuessesMachineThinksGame.ask_for_a_guess', return_value='1111')
    @patch('guessthenumber.thinker.Thinker.think_number', return_value='1111')
    @patch('builtins.print')
    def test_game_hgmtg(self, mocked_print, mocked_think_number, mocked_ask_for_a_guess, mocked_evaluate_guess):

        game = HumanGuessesMachineThinksGame()
        game.play()
        mocked_print.assert_called_once_with(GAME_OVER_MESSAGE)
        mocked_think_number.assert_called_once_with(cipher_quantity=4)
        mocked_ask_for_a_guess.assert_called_once()
        mocked_evaluate_guess.assert_called_once_with('1111', '1111')

    @patch('builtins.input')
    @patch('builtins.print')
    def test_hgmtg_ask_for_a_guess(self, mocked_print, mocked_input):

        game = HumanGuessesMachineThinksGame()
        game.ask_for_a_guess('Some message')
        mocked_print.assert_called_once_with('Some message')
        mocked_input.assert_called_once_with('Please, take a guess: ')

    @patch('guessthenumber.guesser.Guesser.take_a_guess', return_value=None)
    @patch('builtins.print', return_value=GAME_OVER_MESSAGE)
    @patch('builtins.input')
    def test_game_mghtg(self, mocked_input, mocked_print, mocked_take_a_guess):

        game = MachineGuessesHumanThinksGame()
        game.play()

        mocked_input.assert_not_called
        mocked_print.assert_called_once_with(GAME_OVER_MESSAGE)
        mocked_take_a_guess.assert_called_once_with('')


@patch('guessthenumber.common.random.randint', return_value=1)
class TestThinker:

    def test_think_number_four_ciphers(self, mocked_randint):
        assert '1111' == Thinker.think_number()

    def test_think_number_zero_ciphers(self, mocked_randint):
        """Return always 0 if number is cipher quantity is zero."""
        assert '' == Thinker.think_number(cipher_quantity=0)

    def test_think_number_minus_one_ciphers(self, mocked_randint):
        """Return always 0 if number is negative."""
        assert '' == Thinker.think_number(cipher_quantity=-1)


class TestEvaluator:

    def test_evaluate_guess(self):
        answer = Evaluator.evaluate_guess('1234', '1234')

        assert 4 == answer.rights
        assert 0 == answer.wrongs
        assert 0 == answer.present_but_wrong

    def test_evaluate_guess_three_wrongs(self):
        answer = Evaluator.evaluate_guess('1111', '1234')

        assert 1 == answer.rights
        assert 0 == answer.wrongs
        assert 3 == answer.present_but_wrong

    def test_evaluate_guess_two_rights_one_wrong_one_pbw(self):
        answer = Evaluator.evaluate_guess('1234', '1273')

        assert 2 == answer.rights
        assert 1 == answer.wrongs
        assert 1 == answer.present_but_wrong

    def test_evaluate_guess_one_right_three_wrongs(self):
        answer = Evaluator.evaluate_guess('1234', '8564')

        assert 1 == answer.rights
        assert 3 == answer.wrongs
        assert 0 == answer.present_but_wrong

    def test_evaluate_guess_no_rights_four_pbw(self):
        answer = Evaluator.evaluate_guess('1234', '4321')

        assert 0 == answer.rights
        assert 0 == answer.wrongs
        assert 4 == answer.present_but_wrong


class TestAnswer:

    def test_answer_str(self):
        answer = Answer('1111', 3, 1, 0)
        assert 'Rights: 3. Wrongs: 1. Present but wrong: 0.' == str(answer)

    def test_answer_bool_false(self):
        answer = Answer('1111', 3, 1, 0)
        assert not bool(answer)

    def test_answer_bool_true(self):
        answer = Answer('1111', 4, 0, 0)
        assert bool(answer)


class TestGuesser:

    def test_guesser(self):
        guesser = Guesser(5)

        assert guesser.lower_guess == 0
        assert guesser.current_guess is None
        assert guesser.higher_guess == 99999

    def test_guesser_take_a_guess_no_hint(self):
        guesser = Guesser(4)
        guess = guesser.take_a_guess()

        assert guess == 9999 // 2

    def test_guesser_take_a_guess_lower_hint(self):
        guesser = Guesser(4)
        guesser.lower_guess = 1111
        guesser.current_guess = 2222
        guess = guesser.take_a_guess('lower')

        assert guesser.higher_guess == 2222
        assert guess == 3333 // 2

    def test_guesser_take_a_guess_higher_hint(self):
        guesser = Guesser(4)
        guesser.current_guess = 1111
        guesser.higher_guess = 2222
        guess = guesser.take_a_guess('higher')

        assert guesser.lower_guess == 1111
        assert guess == 3333 // 2

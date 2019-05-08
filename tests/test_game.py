from mock import patch

from guessthenumber.game import (
    play,
    take_guess,
    think_number,
)


def test_game():
    assert play()


class TestThinkNumber:

    @patch('guessthenumber.game.random.randint', return_value=1)
    def test_think_number_four_ciphers(self, mocked_randint):
        assert 1111 == think_number()

    @patch('guessthenumber.game.random.randint', return_value=1)
    def test_think_number_zero_ciphers(self, mocked_randint):
        """Return always 0 if number is cipher quantity is zero."""
        assert 0 == think_number(cipher_quantity=0)

    @patch('guessthenumber.game.random.randint', return_value=1)
    def test_think_number_minus_one_ciphers(self, mocked_randint):
        """Return always 0 if number is negative."""
        assert 0 == think_number(cipher_quantity=-1)


class TestTakeGuess:

    def test_take_guess(self):
        answer = take_guess(1234, 1234)

        assert 4 == answer.rights
        assert 0 == answer.wrongs
        assert 0 == answer.present_but_wrong

    def test_take_guess_three_wrongs(self):
        answer = take_guess(1111, 1234)

        assert 1 == answer.rights
        assert 0 == answer.wrongs
        assert 3 == answer.present_but_wrong

    def test_take_guess_two_rights_one_wrong_one_pbw(self):
        answer = take_guess(1234, 1273)

        assert 2 == answer.rights
        assert 1 == answer.wrongs
        assert 1 == answer.present_but_wrong

    def test_take_guess_one_right_three_wrongs(self):
        answer = take_guess(1234, 8564)

        assert 1 == answer.rights
        assert 3 == answer.wrongs
        assert 0 == answer.present_but_wrong

    def test_take_guess_no_rights_four_pbw(self):
        answer = take_guess(1234, 4321)

        assert 0 == answer.rights
        assert 0 == answer.wrongs
        assert 4 == answer.present_but_wrong

from mock import patch

from guessthenumber.game import (
    play,
    think_number,
)


def test_game():
    assert play()

@patch('guessthenumber.game.random.randint', return_value=1)
def test_think_number_four_ciphers(mocked_randint):
    assert 1111 == think_number()

@patch('guessthenumber.game.random.randint', return_value=1)
def test_think_number_zero_ciphers(mocked_randint):
    """Return always 0 if number is cipher quantity is zero."""
    assert 0 == think_number(cipher_quantity=0)

@patch('guessthenumber.game.random.randint', return_value=1)
def test_think_number_minus_one_ciphers(mocked_randint):
    """Return always 0 if number is negative."""
    assert 0 == think_number(cipher_quantity=-1)

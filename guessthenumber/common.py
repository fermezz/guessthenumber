import random


def generate_stringified_random_number(cipher_quantity: int) -> str:
    return ''.join(
        map(
            str, [random.randint(0, 9) for i in range(cipher_quantity)]
        )
    )


def max_cipher_quantity_number(cipher_quantity: int) -> int:
    return int('9' * cipher_quantity)

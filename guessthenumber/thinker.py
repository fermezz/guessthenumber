import random

class Thinker:

    @classmethod
    def think_number(cls, cipher_quantity=4):
        stringified_number = ''.join(
            map(
                str, [random.randint(0, 9) for i in range(cipher_quantity)]
            )
        )

        return int(stringified_number if stringified_number else '0')

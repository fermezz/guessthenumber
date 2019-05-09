from guessthenumber.common import generate_stringified_random_number

class Thinker:

    @classmethod
    def think_number(cls, cipher_quantity=4):
        return generate_stringified_random_number(cipher_quantity)

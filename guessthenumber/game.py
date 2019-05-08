import random


def play():
    return True

def think_number(cipher_quantity=4):
    stringified_number = ''.join(
        map(
            str, [random.randint(0, 9) for i in range(cipher_quantity)]
        )
    )

    return int(stringified_number if stringified_number else '0')


def take_guess(guess, number):
    guess = str(guess)
    number = str(number)

    if guess == number:
        return Answer(len(number), 0, 0)

    rights = 0
    wrongs = 0
    present_but_wrong = 0
    for idx, char in enumerate(guess):
        if char == number[idx]:
            rights += 1
        elif char in number:
            present_but_wrong += 1
        else:
            wrongs += 1

    return Answer(rights, wrongs, present_but_wrong)



class Answer:

    def __init__(self, rights, wrongs, present_but_wrong):
        self.rights = rights
        self.wrongs = wrongs
        self.present_but_wrong = present_but_wrong

    def __str__(self):
        return 'Rights: {rights}. Wrongs: {wrongs}. Present but wrong: {present_but_wrong}.'.format(
            rights=self.rights,
            wrongs=self.wrongs,
            present_but_wrong=self.present_but_wrong,
        )


class Evaluator:

    @classmethod
    def evaluate_guess(cls, guess, number):
        guess = str(guess)
        number = str(number)

        if guess == number:
            return Answer(number, len(number), 0, 0)

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

        return Answer(number, rights, wrongs, present_but_wrong)



class Answer:

    def __init__(self, number, rights, wrongs, present_but_wrong):
        self.number = number
        self.rights = rights
        self.wrongs = wrongs
        self.present_but_wrong = present_but_wrong

    def __str__(self):
        return 'Rights: {rights}. Wrongs: {wrongs}. Present but wrong: {present_but_wrong}.'.format(
            rights=self.rights,
            wrongs=self.wrongs,
            present_but_wrong=self.present_but_wrong,
        )

    def __bool__(self):
        return len(self.number) == self.rights and self.wrongs == 0 and self.present_but_wrong == 0

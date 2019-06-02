from dataclasses import dataclass


@dataclass
class Answer:

    number: str
    rights: int
    wrongs: int
    present_but_wrong: int

    def __str__(self) -> str:
        return 'Rights: {rights}. Wrongs: {wrongs}. Present but wrong: {present_but_wrong}.'.format(
            rights=self.rights,
            wrongs=self.wrongs,
            present_but_wrong=self.present_but_wrong,
        )

    def __bool__(self) -> bool:
        return len(self.number) == self.rights and self.wrongs == 0 and self.present_but_wrong == 0


class Evaluator:

    @classmethod
    def evaluate_guess(cls, guess: str, number: str) -> Answer:
        rights: int = 0
        wrongs: int = 0
        present_but_wrong: int = 0

        if guess == number:
            return Answer(number, len(number), 0, 0)

        for idx, char in enumerate(guess):
            if char == number[idx]:
                rights += 1
            elif char in number:
                present_but_wrong += 1
            else:
                wrongs += 1

        return Answer(number, rights, wrongs, present_but_wrong)

// Internal modules
mod evaluator;
mod common;

use evaluator::Answer;
use evaluator::evaluate_guess;


pub trait Game {
    fn play(self) -> std::result::Result<(), Box<dyn std::error::Error>>;
}

pub struct HumanGuessesMachineThinksGame;

impl Game for HumanGuessesMachineThinksGame {
    fn play(self) -> std::result::Result<(), Box<dyn std::error::Error>> {
        let thought_number = common::generate_stringified_random_number(4);
        println!("Thought number: {}", thought_number);
        let mut guess = ask_for_a_guess();
        let mut answer: Answer = evaluate_guess(&guess, &thought_number);

        loop {
            if answer.is_correct(&guess) {
                break;
            } else {
                println!("{:?}. Try again!", answer);
                guess = ask_for_a_guess();
                answer = evaluate_guess(&guess, &thought_number);
            }
        }

        println!("You win!");

        Ok(())
    }
}

fn ask_for_a_guess() -> String {
    try_read!().unwrap()
}
